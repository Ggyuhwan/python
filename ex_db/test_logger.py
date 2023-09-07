import mylogger

log = mylogger.make_logger()
log.debug('test')
log.info('info test')
log.warning('warning test')

def test(a,b):
    try:
        result = a/b
    except ZeroDivisionError as e:
        log.exception(str(e))
    return result
test(2, 0)
