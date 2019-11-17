#KURILNICA API

## Termometer 1

Prvi termometer bo v peči

'GET /devices/t1'

Trenutna temperetura

Drugi termometer bo v zalogovniku

'GET /devices/t2'

Trenutna temperetura v zalogovniku

'GET /i'

Trenutne informacije o napravah

'GET /getMax/<name>/<day>'

Maxsimalna vrednost naprave za določen dan

<day> -> yyyy-mm-dd

'GET /getMin/<name>/<day>'

Minimalna vrednost naprave za določen dan

<day> -> yyyy-mm-dd

'GET /<name>/<from_>/<to>'

Ime naprave, od_kdaj, do_kdaj

primer klica: /T1/2019-01-01/2019-01-02
