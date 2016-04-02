from tweet import Tweet
import time
import json
import argparse
import logging
import datetime


def main():
    try:
        with open('since_id', 'r') as f:
	    since_id = json.load(f)
    except:
        since_id = 1
	with open('since_id', 'w') as f:
	    json.dump(since_id, f)

    with open('since_id', 'w') as f:
	t = Tweet(since_id=since_id)
	while True:
            try:
                t.maintain()
                logging.debug('ran maintain @ ' + str(datetime.now()))
		sid = t.since_id
		json.dump(since_id, f)
		time.sleep(5*60)
	    except KeyboardInterrupt, e:
		break

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
