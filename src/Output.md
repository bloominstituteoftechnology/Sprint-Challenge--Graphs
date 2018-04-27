| Input                        | Output                                        |
| :--------------------------: | :-------------------------------------------: |
| node routing.js HostA HostD  | HostA --> HostB --> HostD                     |
| node routing.js HostA HostH  | HostA --> HostC --> HostF --> HostH           |
| node routing.js HostA HostA  | Host A                                        |
| node routing.js HostE HostB  | HostE --> HostF --> HostC --> HostA --> HostB |