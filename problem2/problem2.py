def date_format(date: str) -> str: 
    """
    Input - MM/DD/YYYY
    Output - YYYY-MM-DD
    """
    return (date[6:] + '-' + date[:2] + '-' + date[3:5])
