from datetime import date

def season_start_year(as_of: date) -> int: # as_of parameter should be a date; as_of: date
    """return the year for the laliga season the date(whatever "as_of" is) in question is in """
    return as_of.year if as_of.month >=8 else as_of.year - 1


if __name__ == "__main__":
    print(season_start_year(date.today()))
    print(season_start_year(date(2027, 3, 15)))
    print(season_start_year(date(2027, 7, 31)))
    print(season_start_year(date(2027, 8, 1)))