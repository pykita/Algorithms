class BucketSortImpl:
    def sort(self, unsorted_array):

        if not unsorted_array:
            return []

        minValue = [0];
        maxValue = 0;
        for item in unsorted_array:
            if item < minValue:
                minValue = item

            if item > maxValue:
                maxValue = item

        bucketList = xrange(maxValue - minValue + 1);

        for number in unsorted_array:
            bucketList[number - minValue].add(number)

        