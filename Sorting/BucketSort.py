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

        bucketList = [None for item in xrange(maxValue - minValue + 1)];

        for number in unsorted_array:
            bucketList[number - minValue] = number

        return self.buckets_to_single_list(bucketList)

    def get_alg_name(self):
        return 'Bucket sort'

    def buckets_to_single_list(self, bucketList):
        result = []
        for bucket in bucketList:
            if bucket is not None:
                result.append(bucket)

        return result

        