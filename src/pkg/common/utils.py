import time
import datetime
import pandas as pd


def format_date(year, month, date, delimiter=''):
    """
    format_date: reformat report into Y-m-d.
    Args:
        year: year report
        month: month report
        date: date report
        delimiter: delimiter

    Returns:

    """
    current_date = '%s' % date
    # insert 0 if date < 10
    if date < 10:
        current_date = '0%s' % date

    current_month = '%s' % month
    if month < 10:
        current_month = '0%s' % month

    date = '%s%s%s%s%s' % (
        year,
        delimiter,
        current_month,
        delimiter,
        current_date)
    return date


def wait_until_next_run(run_hour, str_format="%d/%m/%Y %H:%M:%S"):
    """
    wait_until_next_run: return time to wait until time run from current time
    Args:
        run_hour: hour to run process
        str_format:

    Returns:

    """
    current_date = datetime.datetime.today()
    next_date = current_date + datetime.timedelta(days=1)
    delta = -1

    # time to run
    time_run = current_date.strftime("%d/%m/%Y") + " " + run_hour
    run_time = time.mktime(datetime.datetime.strptime(time_run,
                                                      str_format).timetuple())
    # current time larger than run_time => wait until next day
    if current_date.timestamp() > run_time:
        time_run = next_date.strftime("%d/%m/%Y") + " " + run_hour
        run_time = time.mktime(datetime.datetime.strptime(time_run,
                                                          str_format).timetuple())
        delta = 0

    # current time
    current_time = time.mktime(datetime.datetime.now().timetuple())
    print("run_time, ", run_time, current_time)
    report_run_date = current_date + datetime.timedelta(days=delta)
    return run_time - current_time, report_run_date.strftime('%Y-%m-%d')


def compare_date(date1, date2, format_str="%Y-%m-%d"):
    """
    compare_date: compare string datetime if date1 larger than date2
    """
    cur_date1 = datetime.datetime.strptime(date1, format_str)
    cur_date2 = datetime.datetime.strptime(date2, format_str)
    return cur_date1 > cur_date2


def compare_date_gte(date1, date2, format_str="%Y-%m-%d"):
    """
    compare_date: compare string datetime if date1 larger than date2
    """
    cur_date1 = datetime.datetime.strptime(date1, format_str)
    cur_date2 = datetime.datetime.strptime(date2, format_str)
    return cur_date1 >= cur_date2


def get_date(delta=-1, format='%Y-%m-%d'):
    """
    return date format [YYYY-mm-dd] from current date with delta
    Args:
        format:
        delta:

    Returns:

    """
    current_date = datetime.datetime.today()
    date_diff = current_date + datetime.timedelta(days=delta)
    return date_diff.strftime(format)


def validate_date_format(date_text, format="%Y-%m-%d"):
    try:
        datetime.datetime.strptime(date_text, format)
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def increase_date(cur_date="", delta=1, format_str="%Y-%m-%d"):
    cur_date1 = datetime.datetime.strptime(cur_date, format_str)
    delta_date = cur_date1 + datetime.timedelta(days=delta)
    return delta_date.strftime(format_str)


def conv_obj_id(obj_id):
    if type(obj_id) is not str:
        return f'{int(obj_id)}'
    else:
        return obj_id.replace(".0", "")


def batch_df(iterable, batch_number=10000):
    """
    split an iterable into mini batch with batch length of batch_number
    supports batch of a pandas dataframe
    usage:
        for i in batch([1,2,3,4,5], batch_number=2):
            print(i)
        
        for idx, mini_data in enumerate(batch(df, batch_number=10)):
            print(idx)
            print(mini_data)
    """
    l = len(iterable)

    for idx in range(0, l, batch_number):
        if isinstance(iterable, pd.DataFrame):
            # dataframe can't split index label, should iter according index
            yield iterable.iloc[idx:min(idx+batch_number, l)]
        else:
            yield iterable[idx:min(idx+batch_number, l)]


def get_env_data_as_dict(path: str) -> dict:
    dct = {}
    with open(path, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            val = line.replace('\n', '').split('=')
            dct[val[0]] = val[1]
        return dct