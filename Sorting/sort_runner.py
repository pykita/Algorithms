import BucketSort, random, timeit, math
import time

max_random_range = 1000000
max_number_count_range = 1000000

max_random_power = int(math.log10(max_random_range))
max__number_count_power = int(math.log10(max_number_count_range))

#generates array of arrays with random elements for sorting test
random_values = [
    [random.randint(0,int(math.pow(10,i))) for r in xrange(int(math.pow(10,j)))]
        for i in xrange(1,max_random_power+1)
        for j in xrange(1,max__number_count_power+1)
]

def sort_run():
    bucket_sort = BucketSort.BucketSortImpl()
    for item in random_values:
        start = time.clock()
        bucket_sort.sort(item)
        end = time.clock()
        print 'Time:{exec_time}, array_len:{array_len}'.format(exec_time=end-start, array_len=len(item))


if __name__ == '__main__':
    sort_run()

