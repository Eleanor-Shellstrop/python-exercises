def median(iterable):
	items = sorted(iterable)
	median_index = (len(items) - 1) // 2
	if len(items) % 2 != 0:
		return items[median_index]
	return (items[median_index] + items[median_index + 1]) / 2