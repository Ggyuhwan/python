# 주기적으로 실행할 수 있게 해주는 스케줄링 라이브러리
# pip install apscheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
# import pytz
# tz = pytz.timezone('Asia/Seoul')
# dt = datetime.datetime.now(tz)
# interval : 특정 주기로 연속적으로 실행할때
# cron     : 원하는 시간, 다양한 시간에 실행해야할때
def test_interval():
    print("interval")
    print(datetime.datetime.now())
def test_cron():
    print("cron")
    # print(datetime.datetime.now())
sched = BlockingScheduler()
# 잡 등록  (10초에 한번씩 함수 호출)
sched.add_job(test_interval, 'interval', seconds=5)
sched.add_job(test_cron, 'cron', hour='11', minute='57')
# 매일 5시에 실행
# sched.add_job(test_cron, 'cron', hour='17')
# 매월 1일 오전 10시 30분
# sched.add_job(test_cron, 'cron', day='1', hour='10', minute='30')
# 월 ~ 금 오후 2시
# sched.add_job(test_cron, 'cron', day_of_week='mon-fri', hour='14')
# 수, 금 만 9시에
# sched.add_job(test_cron, 'cron', day_of_week='wed,fri', hour='09')
# 매년 1월 1일 자정
# sched.add_job(test_cron, 'cron', month='1', day='1', hour='0')
sched.start()