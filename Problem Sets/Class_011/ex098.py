def transform(lst):
    result = []
    for sublist in lst:
        transformed_sublist = []
        for item in sublist:
            try:
                transformed_sublist.append(1 / int(item))
            except Exception as e:
                print(f"""Error: {type(e).__name__} for value "{item}": {str(e)}.""")

        if transformed_sublist:
            result.append(transformed_sublist)

    return result
