def get_old_files(date: str):
    query = "modifiedTime < '{}'".format(date)
    print(query)


print(get_old_files('2019-06-04'))
