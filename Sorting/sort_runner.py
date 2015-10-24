import BucketSort, random, timeit

random_values = [
    random.randint(0,1000) for r in xrange(10),
    random.randint(0,1000) for r in xrange(1000),
    random.randint(0,1000) for r in xrange(1000000),
    random.randint(0,100) for r in xrange(10),
    random.randint(0,10000) for r in xrange(10),
    random.randint(0,1000000) for r in xrange(10),
]

def sort_run():
    bucket_sort = BucketSort.BucketSortImpl()
    for item in random_values:
        print(timeit.timeit("bucket_sort.sort(item)"))


if __name__ == '__main__':
    print []
    # sort_run()

