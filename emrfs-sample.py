import sys

from pyspark.sql import SparkSession


def main():

    host = sys.argv[1]
    path = sys.argv[2] if len(sys.argv) > 2 else 'sample'
    row_size = int(sys.argv[3]) if len(sys.argv) > 3 else 1000
    column_size = int(sys.argv[4]) if len(sys.argv) > 4 else 10

    print('                     ▎ ▁▁▃▋                            ◢                    ')
    print('                     ▏◢  ▋▎                       ▃▃▄▄▎▎    ◢◢              ')
    print('                   ▉◢    ▊▎                      ◢◢    ▏  ◢◢           ▁  ')
    print('                   ▋      ▋▏                    ▄▄      ▎ ◤      ▂▅▃▅▎')
    print('                   ▋      ▌                    ◢◢       ▊◢ ▁▄▄▆         ')
    print('                   ▊▏     ▍                 ◢◢         ◢◢▄▄▆▆         ▋   ')
    print('                   ▊▎   ▊▊▎▂▄▄▄▄▄▁  ▄▄       ▃▃◤               ▋▏  ')
    print('                    ▋     ◢▇           ▆◣        ▄▄                 ▊▎   ')
    print('                    ▊◢◢                          ▄▄                    ▌    ')
    print('                     ◤◤   ▁              ▁▁▂   ◥                     ▌      ')
    print('                   ◤◤   ▄▄▆▄▄           ◤◤▆▆◥◥◣◣  ◣◣                  ▊▏     ')
    print('                  ◤◤   ▍▅▅▄▄▋          ▍▅▅▆▆▊   ◣◣                  ▍      ')
    print('                       ◥◥   ◤            ◣   ◢◢   ▋                ▋        ')
    print('               ▃▃  ◢◢  ◥◥    ◥◥ ▁▃▃   ◤◤    ◢◢  ◣▎▎            ▂▄▎       ')
    print('            ▄▄▄◢◢ ▏  ▉       ▆   ▆ ▆▆     ▏  █▏▏      ▃▄▄▆           ')
    print('            ▄▄     ◣◣  █     ▉▎▄▃ ▍          ▊▍▄▄▆                   ')
    print('             ▍      ◣◣◤      ▊▏  ▋▏      ◣▂▂◢◢ ◣◣                        ')
    print('            ▉▎      ◣◣         ▄▄  ▄▄           ◢◢   ◣◣                       ')
    print('             ▋         ◣◣         ▆         ▂▂▄▄▍    ◣◣                      ')
    print('              ▌         ◣◣                  ◤◤ ▄▄◣◣     ▄▄                     ')
    print('               ◣◣                                 ▄▄       ▄▄                   ')
    print('                ◣◣                                  ◣◣   ▄▄▄                   ')
    print('                 ◣◣                        ◣◣        ◣◣▄▄                       ')

    spark = SparkSession\
        .builder\
        .appName("pyspark-sample")\
        .getOrCreate()

    # generate test data
    data = list()
    for i in range(row_size):
        row = dict()
        for j in range(column_size):
            row[f'col_{j}'] = i
        data.append(row)

    # create dataframe and write
    df = spark.createDataFrame(data)
    df.write.parquet(f'{host}/{path}', mode='overwrite', compression='snappy')

    # read from storage and count
    df = spark.read.parquet(f'{host}/{path}')
    total = df.count()

    # print
    df.describe().show(vertical=True)
    print(total)
    print('\n\n\n\n')


if __name__ == "__main__":
    main()
