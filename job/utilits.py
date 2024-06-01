def get_date_range(date_list):
    """
    Находит 2 даты (самую раннюю и самую позднюю)
        и промежуток времени с этих дат.

    Args:
        date_list: список дат.

    Returns:
        Кортеж из самой ранней даты, самой поздней даты
        и промежутка времени между ними.
    """

    if not date_list:
        return None, None, None

    # Сортировка дат в порядке возрастания
    sorted_dates = sorted(date_list)

    # Получение самой ранней и самой поздней дат
    earliest_date = sorted_dates[0]
    latest_date = sorted_dates[-1]

    # Вычисление промежутка времени между датами
    time_delta = latest_date - earliest_date

    return earliest_date, latest_date, time_delta
