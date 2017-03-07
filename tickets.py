# coding: utf-8

"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮组菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2017-01-07
    tickets -dg 成都 南京 2017-01-07
"""

from docopt import docopt
from stations import stations
import requests
from trainscollection import TrainsCollection

def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    #print(arguments)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']

    #构建url
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
        date, from_station, to_station
    )

    #添加verify=False参数不验证整数
    r = requests.get(url, verify=False)
    available_trains = r.json()['data']
    #print(available_trains)

    #获取参数
    options = ''.join([key for key, value in arguments.items() if value is True])

    trains = TrainsCollection(available_trains, options)
    trains.pretty_print()


if __name__ == '__main__':
    cli()