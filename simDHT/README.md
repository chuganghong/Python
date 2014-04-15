simDHT:
-------
A DHT crawler, is not quite based on Kademlia, written in Python, the code is very very simple.

dependencies:
------------
1. [bencode](https://pypi.python.org/pypi/bencode/1.0)


start simDHT on *nix
--------------------
1. `python simDHT.py`


stop simDHT on *nix
-------------------
1. `ps aux | grep simDHT.py`
2. `kill -9 PID`

UDP "connection" limit using iptables on Linux(example):
--------------------------------------------------------
1. `iptables -A INPUT -p udp -m limit --limit 500/s --limit-burst 1000 -j RETURN`
2. `iptables -A INPUT -p udp -j DROP`

note:
-----
1. `infohash` is saved in the `infohash.log`.
2. Please on the server running simDHT with a public IP.
