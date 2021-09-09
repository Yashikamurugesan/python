Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data=pd.read_csv('f://DATA SCIENCE NOTES/nba.csv')
>>> 
>>> data
              Name            Team  ...            College     Salary
0    Avery Bradley  Boston Celtics  ...              Texas  7730337.0
1      Jae Crowder  Boston Celtics  ...          Marquette  6796117.0
2     John Holland  Boston Celtics  ...  Boston University        NaN
3      R.J. Hunter  Boston Celtics  ...      Georgia State  1148640.0
4    Jonas Jerebko  Boston Celtics  ...                NaN  5000000.0
..             ...             ...  ...                ...        ...
452     Trey Lyles       Utah Jazz  ...           Kentucky  2239800.0
453   Shelvin Mack       Utah Jazz  ...             Butler  2433333.0
454      Raul Neto       Utah Jazz  ...                NaN   900000.0
455   Tibor Pleiss       Utah Jazz  ...                NaN  2900000.0
456    Jeff Withey       Utah Jazz  ...             Kansas   947276.0

[457 rows x 9 columns]
>>> df=data.dropna()
>>> df
              Name            Team  Number  ... Weight        College     Salary
0    Avery Bradley  Boston Celtics       0  ...    180          Texas  7730337.0
1      Jae Crowder  Boston Celtics      99  ...    235      Marquette  6796117.0
3      R.J. Hunter  Boston Celtics      28  ...    185  Georgia State  1148640.0
6    Jordan Mickey  Boston Celtics      55  ...    235            LSU  1170960.0
7     Kelly Olynyk  Boston Celtics      41  ...    238        Gonzaga  2165160.0
..             ...             ...     ...  ...    ...            ...        ...
449    Rodney Hood       Utah Jazz       5  ...    206           Duke  1348440.0
451  Chris Johnson       Utah Jazz      23  ...    206         Dayton   981348.0
452     Trey Lyles       Utah Jazz      41  ...    234       Kentucky  2239800.0
453   Shelvin Mack       Utah Jazz       8  ...    203         Butler  2433333.0
456    Jeff Withey       Utah Jazz      24  ...    231         Kansas   947276.0

[364 rows x 9 columns]
>>> print(df.to_string())
                         Name                    Team  Number Position  Age  Height  Weight                College      Salary
0               Avery Bradley          Boston Celtics       0       PG   25  06-Feb     180                  Texas   7730337.0
1                 Jae Crowder          Boston Celtics      99       SF   25  06-Jun     235              Marquette   6796117.0
3                 R.J. Hunter          Boston Celtics      28       SG   22  06-May     185          Georgia State   1148640.0
6               Jordan Mickey          Boston Celtics      55       PF   21  06-Aug     235                    LSU   1170960.0
7                Kelly Olynyk          Boston Celtics      41        C   25  Jul-00     238                Gonzaga   2165160.0
8                Terry Rozier          Boston Celtics      12       PG   22  06-Feb     190             Louisville   1824360.0
9                Marcus Smart          Boston Celtics      36       PG   22  06-Apr     220         Oklahoma State   3431040.0
10            Jared Sullinger          Boston Celtics       7        C   24  06-Sep     260             Ohio State   2569260.0
11              Isaiah Thomas          Boston Celtics       4       PG   27  05-Sep     185             Washington   6912869.0
12                Evan Turner          Boston Celtics      11       SG   27  06-Jul     220             Ohio State   3425510.0
13                James Young          Boston Celtics      13       SG   20  06-Jun     215               Kentucky   1749840.0
14               Tyler Zeller          Boston Celtics      44        C   26  Jul-00     253         North Carolina   2616975.0
16               Markel Brown           Brooklyn Nets      22       SG   24  06-Mar     190         Oklahoma State    845059.0
17            Wayne Ellington           Brooklyn Nets      21       SG   28  06-Apr     200         North Carolina   1500000.0
18    Rondae Hollis-Jefferson           Brooklyn Nets      24       SG   21  06-Jul     220                Arizona   1335480.0
19               Jarrett Jack           Brooklyn Nets       2       PG   32  06-Mar     200           Georgia Tech   6300000.0
21            Sean Kilpatrick           Brooklyn Nets       6       SG   26  06-Apr     219             Cincinnati    134215.0
22               Shane Larkin           Brooklyn Nets       0       PG   23  05-Nov     175             Miami (FL)   1500000.0
23                Brook Lopez           Brooklyn Nets      11        C   28  Jul-00     275               Stanford  19689000.0
24           Chris McCullough           Brooklyn Nets       1       PF   21  06-Nov     200               Syracuse   1140240.0
25                Willie Reed           Brooklyn Nets      33       PF   26  06-Oct     220            Saint Louis    947276.0
26            Thomas Robinson           Brooklyn Nets      41       PF   25  06-Oct     237                 Kansas    981348.0
27                 Henry Sims           Brooklyn Nets      14        C   26  06-Oct     248             Georgetown    947276.0
28               Donald Sloan           Brooklyn Nets      15       PG   28  06-Mar     205              Texas A&M    947276.0
29             Thaddeus Young           Brooklyn Nets      30       PF   27  06-Aug     221           Georgia Tech  11235955.0
30              Arron Afflalo         New York Knicks       4       SG   30  06-May     210                   UCLA   8000000.0
31               Lou Amundson         New York Knicks      17       PF   33  06-Sep     220                   UNLV   1635476.0
33            Carmelo Anthony         New York Knicks       7       SF   32  06-Aug     240               Syracuse  22875000.0
35           Cleanthony Early         New York Knicks      11       SF   25  06-Aug     210          Wichita State    845059.0
36          Langston Galloway         New York Knicks       2       SG   24  06-Feb     200         Saint Joseph's    845059.0
37               Jerian Grant         New York Knicks      13       PG   23  06-Apr     195             Notre Dame   1572360.0
38                Robin Lopez         New York Knicks       8        C   28  Jul-00     255               Stanford  12650000.0
39               Kyle O'Quinn         New York Knicks       9       PF   26  06-Oct     250          Norfolk State   3750000.0
42               Lance Thomas         New York Knicks      42       SF   28  06-Aug     235                   Duke   1636842.0
44           Derrick Williams         New York Knicks      23       PF   25  06-Aug     240                Arizona   4000000.0
45                Tony Wroten         New York Knicks       5       SG   23  06-Jun     205             Washington    167406.0
47              Isaiah Canaan      Philadelphia 76ers       0       PG   25  Jun-00     201           Murray State    947276.0
48           Robert Covington      Philadelphia 76ers      33       SF   25  06-Sep     215        Tennessee State   1000000.0
49                Joel Embiid      Philadelphia 76ers      21        C   22  Jul-00     250                 Kansas   4626960.0
50               Jerami Grant      Philadelphia 76ers      39       SF   22  06-Aug     210               Syracuse    845059.0
51             Richaun Holmes      Philadelphia 76ers      22       PF   22  06-Oct     245          Bowling Green   1074169.0
52                Carl Landry      Philadelphia 76ers       7       PF   32  06-Sep     248                 Purdue   6500000.0
53           Kendall Marshall      Philadelphia 76ers       5       PG   24  06-Apr     200         North Carolina   2144772.0
54             T.J. McConnell      Philadelphia 76ers      12       PG   24  06-Feb     200                Arizona    525093.0
55               Nerlens Noel      Philadelphia 76ers       4       PF   22  06-Nov     228               Kentucky   3457800.0
56              Jahlil Okafor      Philadelphia 76ers       8        C   20  06-Nov     275                   Duke   4582680.0
57                  Ish Smith      Philadelphia 76ers       1       PG   27  Jun-00     175            Wake Forest    947276.0
58               Nik Stauskas      Philadelphia 76ers      11       SG   22  06-Jun     205               Michigan   2869440.0
59            Hollis Thompson      Philadelphia 76ers      31       SG   25  06-Aug     206             Georgetown    947276.0
60             Christian Wood      Philadelphia 76ers      35       PF   20  06-Nov     220                   UNLV    525093.0
63            DeMarre Carroll         Toronto Raptors       5       SF   29  06-Aug     212               Missouri  13600000.0
64              DeMar DeRozan         Toronto Raptors      10       SG   26  06-Jul     220                    USC  10050000.0
65              James Johnson         Toronto Raptors       3       PF   29  06-Sep     250            Wake Forest   2500000.0
66                Cory Joseph         Toronto Raptors       6       PG   24  06-Mar     190                  Texas   7000000.0
67                 Kyle Lowry         Toronto Raptors       7       PG   30  Jun-00     205              Villanova  12000000.0
69          Patrick Patterson         Toronto Raptors      54       PF   27  06-Sep     235               Kentucky   6268675.0
70              Norman Powell         Toronto Raptors      24       SG   23  06-Apr     215                   UCLA    650000.0
71              Terrence Ross         Toronto Raptors      31       SF   25  06-Jul     195             Washington   3553917.0
73             Jason Thompson         Toronto Raptors       1       PF   29  06-Nov     250                  Rider    245177.0
75               Delon Wright         Toronto Raptors      55       PG   24  06-May     190                   Utah   1509360.0
77            Harrison Barnes   Golden State Warriors      40       SF   24  06-Aug     225         North Carolina   3873398.0
78               Andrew Bogut   Golden State Warriors      12        C   31  Jul-00     260                   Utah  13800000.0
79                  Ian Clark   Golden State Warriors      21       SG   25  06-Mar     175                Belmont    947276.0
80              Stephen Curry   Golden State Warriors      30       PG   28  06-Mar     190               Davidson  11370786.0
81               Festus Ezeli   Golden State Warriors      31        C   26  06-Nov     265             Vanderbilt   2008748.0
82             Draymond Green   Golden State Warriors      23       PF   26  06-Jul     230         Michigan State  14260870.0
83             Andre Iguodala   Golden State Warriors       9       SF   32  06-Jun     215                Arizona  11710456.0
85               Kevon Looney   Golden State Warriors      36       SF   20  06-Sep     220                   UCLA   1131960.0
86       James Michael McAdoo   Golden State Warriors      20       SF   23  06-Sep     240         North Carolina    845059.0
87               Brandon Rush   Golden State Warriors       4       SF   30  06-Jun     220                 Kansas   1270964.0
88          Marreese Speights   Golden State Warriors       5        C   28  06-Oct     255                Florida   3815000.0
89              Klay Thompson   Golden State Warriors      11       SG   26  06-Jul     215       Washington State  15501000.0
91               Cole Aldrich    Los Angeles Clippers      45        C   27  06-Nov     250                 Kansas   1100602.0
92                 Jeff Ayres    Los Angeles Clippers      19       PF   29  06-Sep     250          Arizona State    111444.0
93             Jamal Crawford    Los Angeles Clippers      11       SG   36  06-May     195               Michigan   5675000.0
94             Branden Dawson    Los Angeles Clippers      22       SF   23  06-Jun     225         Michigan State    525093.0
95                 Jeff Green    Los Angeles Clippers       8       SF   29  06-Sep     235             Georgetown   9650000.0
96              Blake Griffin    Los Angeles Clippers      32       PF   27  06-Oct     251               Oklahoma  18907726.0
97             Wesley Johnson    Los Angeles Clippers      33       SF   28  06-Jul     215               Syracuse   1100602.0
98             DeAndre Jordan    Los Angeles Clippers       6        C   27  06-Nov     265              Texas A&M  19689000.0
99   Luc Richard Mbah a Moute    Los Angeles Clippers      12       PF   29  06-Aug     230                   UCLA    947276.0
100                Chris Paul    Los Angeles Clippers       3       PG   31  Jun-00     175            Wake Forest  21468695.0
101               Paul Pierce    Los Angeles Clippers      34       SF   38  06-Jul     235                 Kansas   3376000.0
103                 JJ Redick    Los Angeles Clippers       4       SG   31  06-Apr     190                   Duke   7085000.0
104             Austin Rivers    Los Angeles Clippers      25       PG   23  06-Apr     200                   Duke   3110796.0
105               C.J. Wilcox    Los Angeles Clippers      30       SG   25  06-May     195             Washington   1159680.0
106              Brandon Bass      Los Angeles Lakers       2       PF   31  06-Aug     250                    LSU   3000000.0
107               Tarik Black      Los Angeles Lakers      28        C   24  06-Sep     250                 Kansas    845059.0
108             Anthony Brown      Los Angeles Lakers       3       SF   23  06-Jul     210               Stanford    700000.0
110           Jordan Clarkson      Los Angeles Lakers       6       PG   24  06-May     194               Missouri    845059.0
111               Roy Hibbert      Los Angeles Lakers      17        C   29  07-Feb     270             Georgetown  15592217.0
113                Ryan Kelly      Los Angeles Lakers       4       PF   25  06-Nov     230                   Duke   1724250.0
114           Larry Nance Jr.      Los Angeles Lakers       7       PF   23  06-Sep     230                Wyoming   1155600.0
115             Julius Randle      Los Angeles Lakers      30       PF   21  06-Sep     250               Kentucky   3132240.0
116          D'Angelo Russell      Los Angeles Lakers       1       PG   20  06-May     195             Ohio State   5103120.0
117              Robert Sacre      Los Angeles Lakers      50        C   27  Jul-00     270                Gonzaga    981348.0
119         Metta World Peace      Los Angeles Lakers      37       SF   36  06-Jul     260             St. John's    947276.0
120                Nick Young      Los Angeles Lakers       0       SF   31  06-Jul     210                    USC   5219169.0
121              Eric Bledsoe            Phoenix Suns       2       PG   26  06-Jan     190               Kentucky  13500000.0
122              Devin Booker            Phoenix Suns       1       SG   19  06-Jun     206               Kentucky   2127840.0
123            Chase Budinger            Phoenix Suns      10       SF   28  06-Jul     209                Arizona    206192.0
125            Archie Goodwin            Phoenix Suns      20       SG   21  06-May     200               Kentucky   1160160.0
126              John Jenkins            Phoenix Suns      23       SG   25  06-Apr     215             Vanderbilt    981348.0
127            Brandon Knight            Phoenix Suns       3       PG   24  06-Mar     189               Kentucky  13500000.0
128                  Alex Len            Phoenix Suns      21        C   22  07-Jan     260               Maryland   3807120.0
129                 Jon Leuer            Phoenix Suns      30       PF   27  06-Oct     228              Wisconsin   1035000.0
130              Phil Pressey            Phoenix Suns      25       PG   25  05-Nov     175               Missouri     55722.0
131              Ronnie Price            Phoenix Suns      14       PG   32  06-Feb     190            Utah Valley    947276.0
133               P.J. Tucker            Phoenix Suns      17       SF   31  06-Jun     245                  Texas   5500000.0
134               T.J. Warren            Phoenix Suns      12       SF   22  06-Aug     230   North Carolina State   2041080.0
135             Alan Williams            Phoenix Suns      15        C   23  06-Aug     260       UC Santa Barbara     83397.0
136                Quincy Acy        Sacramento Kings      13       SF   25  06-Jul     240                 Baylor    981348.0
137            James Anderson        Sacramento Kings       5       SG   27  06-Jun     213         Oklahoma State   1015421.0
139              Caron Butler        Sacramento Kings      31       SF   36  06-Jul     228            Connecticut   1449187.0
141       Willie Cauley-Stein        Sacramento Kings       0        C   22  Jul-00     240               Kentucky   3398280.0
142           Darren Collison        Sacramento Kings       7       PG   28  Jun-00     175                   UCLA   5013559.0
143          DeMarcus Cousins        Sacramento Kings      15        C   25  06-Nov     270               Kentucky  15851950.0
144                Seth Curry        Sacramento Kings      30       SG   25  06-Feb     185                   Duke    947276.0
145                Duje Dukan        Sacramento Kings      26       PF   24  06-Sep     220              Wisconsin    525093.0
146                  Rudy Gay        Sacramento Kings       8       SF   29  06-Aug     230            Connecticut  12403101.0
147              Kosta Koufos        Sacramento Kings      41        C   27  Jul-00     265             Ohio State   7700000.0
148              Ben McLemore        Sacramento Kings      23       SG   23  06-May     195                 Kansas   3156600.0
149             Eric Moreland        Sacramento Kings      25       PF   24  06-Oct     238           Oregon State    845059.0
150               Rajon Rondo        Sacramento Kings       9       PG   30  06-Jan     186               Kentucky   9500000.0
151          Cameron Bairstow           Chicago Bulls      41       PF   25  06-Sep     250             New Mexico    845059.0
152              Aaron Brooks           Chicago Bulls       0       PG   31  Jun-00     161                 Oregon   2250000.0
153              Jimmy Butler           Chicago Bulls      21       SG   26  06-Jul     220              Marquette  16407500.0
154             Mike Dunleavy           Chicago Bulls      34       SG   35  06-Sep     230                   Duke   4500000.0
157                Taj Gibson           Chicago Bulls      22       PF   30  06-Sep     225                    USC   8500000.0
158            Justin Holiday           Chicago Bulls       7       SG   27  06-Jun     185             Washington    947276.0
159            Doug McDermott           Chicago Bulls       3       SF   24  06-Aug     225              Creighton   2380440.0
161             E'Twaun Moore           Chicago Bulls      55       SG   27  06-Apr     191                 Purdue   1015421.0
162               Joakim Noah           Chicago Bulls      13        C   31  06-Nov     232                Florida  13400000.0
163              Bobby Portis           Chicago Bulls       5       PF   21  06-Nov     230               Arkansas   1391160.0
164              Derrick Rose           Chicago Bulls       1       PG   27  06-Mar     190                Memphis  20093064.0
165                Tony Snell           Chicago Bulls      20       SF   24  06-Jul     200             New Mexico   1535880.0
166       Matthew Dellavedova     Cleveland Cavaliers       8       PG   25  06-Apr     198           Saint Mary's   1147276.0
167             Channing Frye     Cleveland Cavaliers       9       PF   33  06-Nov     255                Arizona   8193029.0
168              Kyrie Irving     Cleveland Cavaliers       2       PG   24  06-Mar     193                   Duke  16407501.0
170         Richard Jefferson     Cleveland Cavaliers      24       SF   35  06-Jul     233                Arizona    947276.0
172               James Jones     Cleveland Cavaliers       1       SG   35  06-Aug     218             Miami (FL)    947276.0
173                Sasha Kaun     Cleveland Cavaliers      14        C   31  06-Nov     260                 Kansas   1276000.0
174                Kevin Love     Cleveland Cavaliers       0       PF   27  06-Oct     251                   UCLA  19689000.0
175              Jordan McRae     Cleveland Cavaliers      12       SG   25  06-May     179              Tennessee    111196.0
177             Iman Shumpert     Cleveland Cavaliers       4       SG   25  06-May     220           Georgia Tech   8988765.0
179          Tristan Thompson     Cleveland Cavaliers      13        C   25  06-Sep     238                  Texas  14260870.0
180               Mo Williams     Cleveland Cavaliers      52       PG   33  06-Jan     198                Alabama   2100000.0
181              Joel Anthony         Detroit Pistons      50        C   33  06-Sep     245                   UNLV   2500000.0
182               Aron Baynes         Detroit Pistons      12        C   29  06-Oct     260       Washington State   6500000.0
183               Steve Blake         Detroit Pistons      22       PG   36  06-Mar     172               Maryland   2170465.0
184             Lorenzo Brown         Detroit Pistons      17       PG   25  06-May     189   North Carolina State    111444.0
185            Reggie Bullock         Detroit Pistons      25       SF   25  06-Jul     205         North Carolina   1252440.0
186  Kentavious Caldwell-Pope         Detroit Pistons       5       SG   23  06-May     205                Georgia   2891760.0
187         Spencer Dinwiddie         Detroit Pistons       8       PG   23  06-Jun     200               Colorado    845059.0
188            Andre Drummond         Detroit Pistons       0        C   22  06-Nov     279            Connecticut   3272091.0
189             Tobias Harris         Detroit Pistons      34       SF   23  06-Sep     235              Tennessee  16000000.0
190           Darrun Hilliard         Detroit Pistons       6       SF   23  06-Jun     205              Villanova    600000.0
191            Reggie Jackson         Detroit Pistons       1       PG   26  06-Mar     208         Boston College  13913044.0
192           Stanley Johnson         Detroit Pistons       3       SF   20  06-Jul     245                Arizona   2841960.0
193               Jodie Meeks         Detroit Pistons      20       SG   28  06-Apr     210               Kentucky   6270000.0
194             Marcus Morris         Detroit Pistons      13       PF   26  06-Sep     235                 Kansas   5000000.0
195          Anthony Tolliver         Detroit Pistons      43       PF   31  06-Aug     240              Creighton   3000000.0
196               Lavoy Allen          Indiana Pacers       5       PF   27  06-Sep     255                 Temple   4050000.0
197          Rakeem Christmas          Indiana Pacers      25       PF   24  06-Sep     250               Syracuse   1007026.0
199               Paul George          Indiana Pacers      13       SF   26  06-Sep     220           Fresno State  17120106.0
200               George Hill          Indiana Pacers       3       PG   30  06-Mar     188                  IUPUI   8000000.0
201               Jordan Hill          Indiana Pacers      27        C   28  06-Oct     235                Arizona   4000000.0
202              Solomon Hill          Indiana Pacers      44       SF   25  06-Jul     225                Arizona   1358880.0
203                 Ty Lawson          Indiana Pacers      10       PG   28  05-Nov     195         North Carolina    211744.0
206        Glenn Robinson III          Indiana Pacers      40       SG   22  06-Jul     222               Michigan   1100000.0
207            Rodney Stuckey          Indiana Pacers       2       PG   30  06-May     205     Eastern Washington   7000000.0
208              Myles Turner          Indiana Pacers      33       PF   20  06-Nov     243                  Texas   2357760.0
209        Shayne Whittington          Indiana Pacers      42       PF   25  06-Nov     250       Western Michigan    845059.0
210                 Joe Young          Indiana Pacers       1       PG   23  06-Feb     180                 Oregon   1007026.0
212            Jerryd Bayless         Milwaukee Bucks      19       PG   27  06-Mar     200                Arizona   3000000.0
213   Michael Carter-Williams         Milwaukee Bucks       5       PG   24  06-Jun     190               Syracuse   2399040.0
214          Jared Cunningham         Milwaukee Bucks       9       SG   25  06-Apr     195           Oregon State    947276.0
215               Tyler Ennis         Milwaukee Bucks      11       PG   21  06-Mar     194               Syracuse   1662360.0
216               John Henson         Milwaukee Bucks      31       PF   25  06-Nov     229         North Carolina   2943221.0
218                 O.J. Mayo         Milwaukee Bucks       3       SG   28  06-May     210                    USC   8000000.0
219           Khris Middleton         Milwaukee Bucks      22       SG   24  06-Aug     234              Texas A&M  14700000.0
220               Greg Monroe         Milwaukee Bucks      15        C   26  06-Nov     265             Georgetown  16407500.0
221               Steve Novak         Milwaukee Bucks       6       SF   32  06-Oct     225              Marquette    295327.0
222       Johnny O'Bryant III         Milwaukee Bucks      77       PF   23  06-Sep     257                    LSU    845059.0
223             Jabari Parker         Milwaukee Bucks      12       PF   21  06-Aug     250                   Duke   5152440.0
224             Miles Plumlee         Milwaukee Bucks      18        C   27  06-Nov     249                   Duke   2109294.0
225           Greivis Vasquez         Milwaukee Bucks      21       PG   29  06-Jun     217               Maryland   6600000.0
226             Rashad Vaughn         Milwaukee Bucks      20       SG   19  06-Jun     202                   UNLV   1733040.0
227           Justin Anderson        Dallas Mavericks       1       SG   22  06-Jun     228               Virginia   1449000.0
228                J.J. Barea        Dallas Mavericks       5       PG   31  Jun-00     185           Northeastern   4290000.0
229              Jeremy Evans        Dallas Mavericks      21       SF   28  06-Sep     200       Western Kentucky   1100602.0
230            Raymond Felton        Dallas Mavericks       2       PG   31  06-Jan     205         North Carolina   3950313.0
231              Devin Harris        Dallas Mavericks      34       PG   33  06-Mar     185              Wisconsin   4053446.0
232                 David Lee        Dallas Mavericks      42       PF   33  06-Sep     245                Florida   2085671.0
233           Wesley Matthews        Dallas Mavericks      23       SG   29  06-May     220              Marquette  16407500.0
234              JaVale McGee        Dallas Mavericks      11        C   28  Jul-00     270                 Nevada   1270964.0
238          Chandler Parsons        Dallas Mavericks      25       SF   27  06-Oct     230                Florida  15361500.0
239             Dwight Powell        Dallas Mavericks       7       PF   24  06-Nov     240               Stanford    845059.0
240        Charlie Villanueva        Dallas Mavericks       3       PF   31  06-Nov     232            Connecticut    947276.0
241            Deron Williams        Dallas Mavericks       8       PG   31  06-Mar     200               Illinois   5378974.0
242              Trevor Ariza         Houston Rockets       1       SF   30  06-Aug     215                   UCLA   8193030.0
243           Michael Beasley         Houston Rockets       8       SF   27  06-Oct     235           Kansas State    306527.0
244          Patrick Beverley         Houston Rockets       2       PG   27  06-Jan     185               Arkansas   6486486.0
245              Corey Brewer         Houston Rockets      33       SG   30  06-Sep     186                Florida   8229375.0
247                Sam Dekker         Houston Rockets       7       SF   22  06-Sep     230              Wisconsin   1646400.0
248          Andrew Goudelock         Houston Rockets       0       PG   27  06-Mar     200             Charleston    200600.0
249              James Harden         Houston Rockets      13       SG   26  06-May     220          Arizona State  15756438.0
250          Montrezl Harrell         Houston Rockets      35       PF   22  06-Aug     240             Louisville   1000000.0
252            Terrence Jones         Houston Rockets       6       PF   24  06-Sep     252               Kentucky   2489530.0
253            K.J. McDaniels         Houston Rockets      32       SG   23  06-Jun     205                Clemson   3189794.0
256               Jason Terry         Houston Rockets      31       SG   38  06-Feb     185                Arizona    947276.0
257              Jordan Adams       Memphis Grizzlies       3       SG   21  06-May     209                   UCLA   1404600.0
258                Tony Allen       Memphis Grizzlies       9       SG   34  06-Apr     213         Oklahoma State   5158539.0
259            Chris Andersen       Memphis Grizzlies       7       PF   37  06-Oct     245          Blinn College   5000000.0
260               Matt Barnes       Memphis Grizzlies      22       SF   36  06-Jul     226                   UCLA   3542500.0
261              Vince Carter       Memphis Grizzlies      15       SG   39  06-Jun     220         North Carolina   4088019.0
262               Mike Conley       Memphis Grizzlies      11       PG   28  06-Jan     175             Ohio State   9588426.0
263              Bryce Cotton       Memphis Grizzlies       8       PG   23  06-Jan     165             Providence    700902.0
266            JaMychal Green       Memphis Grizzlies       0       PF   25  06-Sep     227                Alabama    845059.0
267             P.J. Hairston       Memphis Grizzlies      19       SF   23  06-Jun     230         North Carolina   1201440.0
268             Jarell Martin       Memphis Grizzlies      10       PF   22  06-Oct     239                    LSU   1230840.0
271             Zach Randolph       Memphis Grizzlies      50       PF   34  06-Sep     260         Michigan State   9638555.0
272          Lance Stephenson       Memphis Grizzlies       1       SF   25  06-May     230             Cincinnati   9000000.0
274            Brandan Wright       Memphis Grizzlies      34       PF   28  06-Oct     210         North Carolina   5464000.0
276             Ryan Anderson    New Orleans Pelicans      33       PF   28  06-Oct     240             California   8500000.0
278              Luke Babbitt    New Orleans Pelicans       8       SF   26  06-Sep     225                 Nevada   1100602.0
279               Norris Cole    New Orleans Pelicans      30       PG   27  06-Feb     175        Cleveland State   3036927.0
280          Dante Cunningham    New Orleans Pelicans      44       PF   29  06-Aug     230              Villanova   2850000.0
281             Anthony Davis    New Orleans Pelicans      23       PF   23  06-Oct     253               Kentucky   7070730.0
282        Bryce Dejean-Jones    New Orleans Pelicans      31       SG   23  06-Jun     203             Iowa State    169883.0
283             Toney Douglas    New Orleans Pelicans      16       PG   30  06-Feb     195          Florida State   1164858.0
284               James Ennis    New Orleans Pelicans       4       SF   25  06-Jul     210       Long Beach State    845059.0
285              Tyreke Evans    New Orleans Pelicans       1       SG   26  06-Jun     220                Memphis  10734586.0
286               Tim Frazier    New Orleans Pelicans       2       PG   25  06-Jan     170             Penn State    845059.0
287                Alonzo Gee    New Orleans Pelicans      15       SF   29  06-Jun     225                Alabama   1320000.0
288               Eric Gordon    New Orleans Pelicans      10       SG   27  06-Apr     215                Indiana  15514031.0
289           Jordan Hamilton    New Orleans Pelicans      25       SG   25  06-Jul     220                  Texas   1015421.0
290              Jrue Holiday    New Orleans Pelicans      11       PG   25  06-Apr     205                   UCLA  10595507.0
291           Orlando Johnson    New Orleans Pelicans       0       SG   27  06-May     220       UC Santa Barbara     55722.0
293          Quincy Pondexter    New Orleans Pelicans      20       SF   28  06-Jul     220             Washington   3382023.0
294         LaMarcus Aldridge       San Antonio Spurs      12       PF   30  06-Nov     240                  Texas  19689000.0
295             Kyle Anderson       San Antonio Spurs       1       SF   22  06-Sep     230                   UCLA   1142880.0
296               Matt Bonner       San Antonio Spurs      15        C   36  06-Oct     235                Florida    947276.0
298                Tim Duncan       San Antonio Spurs      21        C   40  06-Nov     250            Wake Forest   5250000.0
300               Danny Green       San Antonio Spurs      14       SG   28  06-Jun     215         North Carolina  10000000.0
301             Kawhi Leonard       San Antonio Spurs       2       SF   24  06-Jul     230        San Diego State  16407500.0
303              Kevin Martin       San Antonio Spurs      23       SG   33  06-Jul     199       Western Carolina    200600.0
304              Andre Miller       San Antonio Spurs      24       PG   40  06-Mar     200                   Utah    250750.0
305               Patty Mills       San Antonio Spurs       8       PG   27  Jun-00     185           Saint Mary's   3578947.0
307          Jonathon Simmons       San Antonio Spurs      17       SG   26  06-Jun     195                Houston    525093.0
308                David West       San Antonio Spurs      30       PF   35  06-Sep     250                 Xavier   1499187.0
309             Kent Bazemore           Atlanta Hawks      24       SF   26  06-May     201           Old Dominion   2000000.0
310          Tim Hardaway Jr.           Atlanta Hawks      10       SG   24  06-Jun     205               Michigan   1304520.0
311              Kirk Hinrich           Atlanta Hawks      12       SG   35  06-Apr     190                 Kansas   2854940.0
312                Al Horford           Atlanta Hawks      15        C   30  06-Oct     245                Florida  12000000.0
313            Kris Humphries           Atlanta Hawks      43       PF   31  06-Sep     235              Minnesota   1000000.0
314               Kyle Korver           Atlanta Hawks      26       SG   35  06-Jul     212              Creighton   5746479.0
315              Paul Millsap           Atlanta Hawks       4       PF   31  06-Aug     246         Louisiana Tech  18671659.0
316              Mike Muscala           Atlanta Hawks      31       PF   24  06-Nov     240               Bucknell    947276.0
317           Lamar Patterson           Atlanta Hawks      13       SG   24  06-May     225             Pittsburgh    525093.0
319                Mike Scott           Atlanta Hawks      32       PF   27  06-Aug     237               Virginia   3333333.0
323               Jeff Teague           Atlanta Hawks       0       PG   27  06-Feb     186            Wake Forest   8000000.0
325              Troy Daniels       Charlotte Hornets      30       SG   24  06-Apr     205  Virginia Commonwealth    947276.0
326           Jorge Gutierrez       Charlotte Hornets      12       PG   27  06-Mar     189             California    189455.0
327          Tyler Hansbrough       Charlotte Hornets      50       PF   30  06-Sep     250         North Carolina    947276.0
328            Aaron Harrison       Charlotte Hornets       9       SG   21  06-Jun     210               Kentucky    525093.0
329             Spencer Hawes       Charlotte Hornets       0       PF   28  07-Jan     245             Washington   6110034.0
331        Frank Kaminsky III       Charlotte Hornets      44        C   23  Jul-00     240              Wisconsin   2612520.0
332    Michael Kidd-Gilchrist       Charlotte Hornets      14       SF   22  06-Jul     232               Kentucky   6331404.0
333               Jeremy Lamb       Charlotte Hornets       3       SG   24  06-May     185            Connecticut   3034356.0
334              Courtney Lee       Charlotte Hornets       1       SG   30  06-May     200       Western Kentucky   5675000.0
335                Jeremy Lin       Charlotte Hornets       7       PG   27  06-Mar     200                Harvard   2139000.0
336              Kemba Walker       Charlotte Hornets      15       PG   26  06-Jan     184            Connecticut  12000000.0
337           Marvin Williams       Charlotte Hornets       2       PF   29  06-Sep     237         North Carolina   7000000.0
338               Cody Zeller       Charlotte Hornets      40        C   23  Jul-00     240                Indiana   4204200.0
339                Chris Bosh              Miami Heat       1       PF   32  06-Nov     235           Georgia Tech  22192730.0
340                 Luol Deng              Miami Heat       9       SF   31  06-Sep     220                   Duke  10151612.0
343             Udonis Haslem              Miami Heat      40       PF   36  06-Aug     235                Florida   2854940.0
344               Joe Johnson              Miami Heat       2       SF   34  06-Jul     240               Arkansas    261894.0
345             Tyler Johnson              Miami Heat       8       SG   24  06-Apr     186           Fresno State    845059.0
346            Josh McRoberts              Miami Heat       4       PF   29  06-Oct     240                   Duke   5543725.0
347           Josh Richardson              Miami Heat       0       SG   22  06-Jun     200              Tennessee    525093.0
349               Dwyane Wade              Miami Heat       3       SG   34  06-Apr     220              Marquette  20000000.0
351          Hassan Whiteside              Miami Heat      21        C   26  Jul-00     265               Marshall    981348.0
352           Justise Winslow              Miami Heat      20       SF   20  06-Jul     225                   Duke   2481720.0
354            Dewayne Dedmon           Orlando Magic       3        C   26  Jul-00     245                    USC    947276.0
356              Aaron Gordon           Orlando Magic       0       PF   20  06-Sep     220                Arizona   4171680.0
360              Devyn Marble           Orlando Magic      11       SF   23  06-Jun     200                   Iowa    845059.0
361            Shabazz Napier           Orlando Magic      13       PG   24  06-Jan     175            Connecticut   1294440.0
362          Andrew Nicholson           Orlando Magic      44       PF   26  06-Sep     250        St. Bonaventure   2380593.0
363            Victor Oladipo           Orlando Magic       5       SG   24  06-Apr     210                Indiana   5192520.0
364             Elfrid Payton           Orlando Magic       4       PG   22  06-Apr     185    Louisiana-Lafayette   2505720.0
365               Jason Smith           Orlando Magic      14       PF   30  Jul-00     240         Colorado State   4300000.0
366            Nikola Vucevic           Orlando Magic       9        C   25  Jul-00     260                    USC  11250000.0
367               C.J. Watson           Orlando Magic      32       PG   32  06-Feb     175              Tennessee   5000000.0
368             Alan Anderson      Washington Wizards       6       SG   33  06-Jun     220         Michigan State   4000000.0
369              Bradley Beal      Washington Wizards       3       SG   22  06-May     207                Florida   5694674.0
370              Jared Dudley      Washington Wizards       1       SF   30  06-Jul     225         Boston College   4375000.0
371              Jarell Eddie      Washington Wizards       8       SG   24  06-Jul     218          Virginia Tech    561716.0
372               Drew Gooden      Washington Wizards      90       PF   34  06-Oct     250                 Kansas   3300000.0
374                JJ Hickson      Washington Wizards      21        C   27  06-Sep     242   North Carolina State    273038.0
376           Markieff Morris      Washington Wizards       5       PF   26  06-Oct     245                 Kansas   8000000.0
377           Kelly Oubre Jr.      Washington Wizards      12       SF   20  06-Jul     205                 Kansas   1920240.0
378           Otto Porter Jr.      Washington Wizards      22       SF   23  06-Aug     198             Georgetown   4662960.0
379            Ramon Sessions      Washington Wizards       7       PG   30  06-Mar     190                 Nevada   2170465.0
380            Garrett Temple      Washington Wizards      17       SG   30  06-Jun     195                    LSU   1100602.0
381           Marcus Thornton      Washington Wizards      15       SF   29  06-Apr     205                    LSU    200600.0
382                 John Wall      Washington Wizards       2       PG   25  06-Apr     195               Kentucky  15851950.0
383            Darrell Arthur          Denver Nuggets       0       PF   28  06-Sep     235                 Kansas   2814000.0
384             D.J. Augustin          Denver Nuggets      12       PG   28  Jun-00     183                  Texas   3000000.0
385               Will Barton          Denver Nuggets       5       SF   25  06-Jun     175                Memphis   3533333.0
386           Wilson Chandler          Denver Nuggets      21       SF   29  06-Aug     225                 DePaul  10449438.0
387            Kenneth Faried          Denver Nuggets      35       PF   26  06-Aug     228         Morehead State  11235955.0
389               Gary Harris          Denver Nuggets      14       SG   21  06-Apr     210         Michigan State   1584480.0
392               Mike Miller          Denver Nuggets       3       SG   36  06-Aug     218                Florida    947276.0
394             Jameer Nelson          Denver Nuggets       1       PG   34  Jun-00     190         Saint Joseph's   4345000.0
396            JaKarr Sampson          Denver Nuggets       9       SG   23  06-Sep     214             St. John's    258489.0
399              Gorgui Dieng  Minnesota Timberwolves       5        C   26  06-Nov     241             Louisville   1474440.0
401                Tyus Jones  Minnesota Timberwolves       1       PG   20  06-Feb     195                   Duke   1282080.0
402               Zach LaVine  Minnesota Timberwolves       8       PG   21  06-May     189                   UCLA   2148360.0
403          Shabazz Muhammad  Minnesota Timberwolves      15       SF   23  06-Jun     223                   UCLA   2056920.0
404             Adreian Payne  Minnesota Timberwolves      33       PF   25  06-Oct     237         Michigan State   1938840.0
406           Tayshaun Prince  Minnesota Timberwolves      12       SF   36  06-Sep     212               Kentucky    947276.0
410        Karl-Anthony Towns  Minnesota Timberwolves      32        C   20  Jul-00     244               Kentucky   5703600.0
411            Andrew Wiggins  Minnesota Timberwolves      22       SG   21  06-Aug     199                 Kansas   5758680.0
412              Steven Adams   Oklahoma City Thunder      12        C   22  Jul-00     255             Pittsburgh   2279040.0
413             Nick Collison   Oklahoma City Thunder       4       PF   35  06-Oct     255                 Kansas   3750000.0
414              Kevin Durant   Oklahoma City Thunder      35       SF   27  06-Sep     240                  Texas  20158622.0
415                Randy Foye   Oklahoma City Thunder       6       SG   32  06-Apr     213              Villanova   3135000.0
416              Josh Huestis   Oklahoma City Thunder      34       SF   24  06-Jul     230               Stanford   1140240.0
418               Enes Kanter   Oklahoma City Thunder      11        C   24  06-Nov     245               Kentucky  16407500.0
419              Mitch McGary   Oklahoma City Thunder      33       PF   24  06-Oct     255               Michigan   1463040.0
420             Nazr Mohammed   Oklahoma City Thunder      13        C   38  06-Oct     250               Kentucky    222888.0
421            Anthony Morrow   Oklahoma City Thunder       2       SG   30  06-May     210           Georgia Tech   3344000.0
422             Cameron Payne   Oklahoma City Thunder      22       PG   21  06-Mar     185           Murray State   2021520.0
423            Andre Roberson   Oklahoma City Thunder      21       SG   24  06-Jul     210               Colorado   1210800.0
424              Kyle Singler   Oklahoma City Thunder       5       SF   28  06-Aug     228                   Duke   4500000.0
425              Dion Waiters   Oklahoma City Thunder       3       SG   24  06-Apr     220               Syracuse   5138430.0
426         Russell Westbrook   Oklahoma City Thunder       0       PG   27  06-Mar     200                   UCLA  16744218.0
427           Cliff Alexander  Portland Trail Blazers      34       PF   20  06-Aug     240                 Kansas    525093.0
428           Al-Farouq Aminu  Portland Trail Blazers       8       SF   25  06-Sep     215            Wake Forest   8042895.0
429           Pat Connaughton  Portland Trail Blazers       5       SG   23  06-May     206             Notre Dame    625093.0
430              Allen Crabbe  Portland Trail Blazers      23       SG   24  06-Jun     210             California    947276.0
431                  Ed Davis  Portland Trail Blazers      17        C   27  06-Oct     240         North Carolina   6980802.0
432          Maurice Harkless  Portland Trail Blazers       4       SF   23  06-Sep     215             St. John's   2894059.0
433          Gerald Henderson  Portland Trail Blazers       9       SG   28  06-May     215                   Duke   6000000.0
434               Chris Kaman  Portland Trail Blazers      35        C   34  Jul-00     265       Central Michigan   5016000.0
435            Meyers Leonard  Portland Trail Blazers      11       PF   24  07-Jan     245               Illinois   3075880.0
436            Damian Lillard  Portland Trail Blazers       0       PG   25  06-Mar     195            Weber State   4236287.0
437             C.J. McCollum  Portland Trail Blazers       3       SG   24  06-Apr     200                 Lehigh   2525160.0
438              Luis Montero  Portland Trail Blazers      44       SG   23  06-Jul     185         Westchester CC    525093.0
439             Mason Plumlee  Portland Trail Blazers      24        C   26  06-Nov     235                   Duke   1415520.0
440             Brian Roberts  Portland Trail Blazers       2       PG   30  06-Jan     173                 Dayton   2854940.0
441               Noah Vonleh  Portland Trail Blazers      21       PF   20  06-Sep     240                Indiana   2637720.0
442             Trevor Booker               Utah Jazz      33       PF   28  06-Aug     228                Clemson   4775000.0
443                Trey Burke               Utah Jazz       3       PG   23  06-Jan     191               Michigan   2658240.0
444                Alec Burks               Utah Jazz      10       SG   24  06-Jun     214               Colorado   9463484.0
446            Derrick Favors               Utah Jazz      15       PF   24  06-Oct     265           Georgia Tech  12000000.0
448            Gordon Hayward               Utah Jazz      20       SF   26  06-Aug     226                 Butler  15409570.0
449               Rodney Hood               Utah Jazz       5       SG   23  06-Aug     206                   Duke   1348440.0
451             Chris Johnson               Utah Jazz      23       SF   26  06-Jun     206                 Dayton    981348.0
452                Trey Lyles               Utah Jazz      41       PF   20  06-Oct     234               Kentucky   2239800.0
453              Shelvin Mack               Utah Jazz       8       PG   26  06-Mar     203                 Butler   2433333.0
456               Jeff Withey               Utah Jazz      24        C   26  Jul-00     231                 Kansas    947276.0
>>> name=['yasi','nave','riya']
>>> age[23,24,13]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    age[23,24,13]
NameError: name 'age' is not defined
>>> name=['yasi','nave','riya']
>>> age=[23,24,13]
>>> roll_no=[23,24,25]
>>> mapped=zip(name,age,roll_no)
>>> print(mapped)
<zip object at 0x0000022875830A40>
>>> for i in mapped():
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    for i in mapped():
TypeError: 'zip' object is not callable
>>> mapped=set(mapped)
>>> print(mapped)
{('nave', 24, 24), ('riya', 13, 25), ('yasi', 23, 23)}
>>> name,age=zip(*mapped)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    name,age=zip(*mapped)
ValueError: too many values to unpack (expected 2)
>>> name,age,roll_no=zip(*mapped)
>>> print(mapped)
{('nave', 24, 24), ('riya', 13, 25), ('yasi', 23, 23)}
>>> print(age)
(24, 13, 23)
>>> print ("The unzipped result: \n",end="")
The unzipped result: 
>>> names,ages,roll_nos=zip(*mapped)
>>> names
('nave', 'riya', 'yasi')
>>> ages
(24, 13, 23)
>>> for i,j in zip(names,ages):
	print(i)

	
nave
riya
yasi
>>> for i,j in zip(names,ages):
	print('names:%s ages:%d' %(i,j))

	
names:nave ages:24
names:riya ages:13
names:yasi ages:23
>>> data=pd.read_csv('f://DATA SCIENCE NOTES/nba.csv')
>>> for i,j in enumerate(data,100):
	print(i,j)

	
100 Name
101 Team
102 Number
103 Position
104 Age
105 Height
106 Weight
107 College
108 Salary
>>> for i,j in enumerate(data,01):
	print(i,j)
	
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> 
>>> for i,j in enumerate(data,10):
	print(i,j)

	
10 Name
11 Team
12 Number
13 Position
14 Age
15 Height
16 Weight
17 College
18 Salary
>>> for i,j in enumerate(data.to_stringa,10):
	print(i,j)

	
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    for i,j in enumerate(data.to_stringa,10):
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\generic.py", line 5478, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'to_stringa'
>>> d=data.to_string()
>>> for i,j in enumerate(d,101):
	print(i,j)

	
101  
102  
103  
104  
105  
106  
107  
108  
109  
110  
111  
112  
113  
114  
115  
116  
117  
118  
119  
120  
121  
122  
123  
124  
125  
126 N
127 a
128 m
129 e
130  
131  
132  
133  
134  
135  
136  
137  
138  
139  
140  
141  
142  
143  
144  
145  
146  
147  
148  
149  
150 T
151 e
152 a
153 m
154  
155  
156 N
157 u
158 m
159 b
160 e
161 r
162  
163 P
164 o
165 s
166 i
167 t
168 i
169 o
170 n
171  
172  
173 A
174 g
175 e
176  
177  
178 H
179 e
180 i
181 g
182 h
183 t
184  
185  
186 W
187 e
188 i
189 g
190 h
191 t
192  
193  
194  
195  
196  
197  
198  
199  
200  
201  
202  
203  
204  
205  
206  
207  
208 C
209 o
210 l
211 l
212 e
213 g
214 e
215  
216  
217  
218  
219  
220  
221 S
222 a
223 l
224 a
225 r
226 y
227 

228 0
229  
230  
231  
232  
233  
234  
235  
236  
237  
238  
239  
240  
241  
242  
243  
244 A
245 v
246 e
247 r
248 y
249  
250 B
251 r
252 a
253 d
254 l
255 e
256 y
257  
258  
259  
260  
261  
262  
263  
264  
265  
266  
267 B
268 o
269 s
270 t
271 o
272 n
273  
274 C
275 e
276 l
277 t
278 i
279 c
280 s
281  
282  
283  
284  
285  
286  
287  
288 0
289  
290  
291  
292  
293  
294  
295  
296 P
297 G
298  
299  
300  
301 2
302 5
303  
304  
305 0
306 6
307 -
308 F
309 e
310 b
311  
312  
313  
314  
315  
316 1
317 8
318 0
319  
320  
321  
322  
323  
324  
325  
326  
327  
328  
329  
330  
331  
332  
333  
334  
335  
336  
337 T
338 e
339 x
340 a
341 s
342  
343  
344  
345 7
346 7
347 3
348 0
349 3
350 3
351 7
352 .
353 0
354 

355 1
356  
357  
358  
359  
360  
361  
362  
363  
364  
365  
366  
367  
368  
369  
370  
371  
372  
373 J
374 a
375 e
376  
377 C
378 r
379 o
380 w
381 d
382 e
383 r
384  
385  
386  
387  
388  
389  
390  
391  
392  
393  
394 B
395 o
396 s
397 t
398 o
399 n
400  
401 C
402 e
403 l
404 t
405 i
406 c
407 s
408  
409  
410  
411  
412  
413  
414 9
415 9
416  
417  
418  
419  
420  
421  
422  
423 S
424 F
425  
426  
427  
428 2
429 5
430  
431  
432 0
433 6
434 -
435 J
436 u
437 n
438  
439  
440  
441  
442  
443 2
444 3
445 5
446  
447  
448  
449  
450  
451  
452  
453  
454  
455  
456  
457  
458  
459  
460 M
461 a
462 r
463 q
464 u
465 e
466 t
467 t
468 e
469  
470  
471  
472 6
473 7
474 9
475 6
476 1
477 1
478 7
479 .
480 0
481 

482 2
483  
484  
485  
486  
487  
488  
489  
490  
491  
492  
493  
494  
495  
496  
497  
498  
499 J
500 o
501 h
502 n
503  
504 H
505 o
506 l
507 l
508 a
509 n
510 d
511  
512  
513  
514  
515  
516  
517  
518  
519  
520  
521 B
522 o
523 s
524 t
525 o
526 n
527  
528 C
529 e
530 l
531 t
532 i
533 c
534 s
535  
536  
537  
538  
539  
540  
541 3
542 0
543  
544  
545  
546  
547  
548  
549  
550 S
551 G
552  
553  
554  
555 2
556 7
557  
558  
559 0
560 6
561 -
562 M
563 a
564 y
565  
566  
567  
568  
569  
570 2
571 0
572 5
573  
574  
575  
576  
577  
578  
579 B
580 o
581 s
582 t
583 o
584 n
585  
586 U
587 n
588 i
589 v
590 e
591 r
592 s
593 i
594 t
595 y
596  
597  
598  
599  
600  
601  
602  
603  
604  
605 N
606 a
607 N
608 

609 3
610  
611  
612  
613  
614  
615  
616  
617  
618  
619  
620  
621  
622  
623  
624  
625  
626  
627 R
628 .
629 J
630 .
631  
632 H
633 u
634 n
635 t
636 e
637 r
638  
639  
640  
641  
642  
643  
644  
645  
646  
647  
648 B
649 o
650 s
651 t
652 o
653 n
654  
655 C
656 e
657 l
658 t
659 i
660 c
661 s
662  
663  
664  
665  
666  
667  
668 2
669 8
670  
671  
672  
673  
674  
675  
676  
677 S
678 G
679  
680  
681  
682 2
683 2
684  
685  
686 0
687 6
688 -
689 M
690 a
691 y
692  
693  
694  
695  
696  
697 1
698 8
699 5
700  
701  
702  
703  
704  
705  
706  
707  
708  
709  
710 G
711 e
712 o
713 r
714 g
715 i
716 a
717  
718 S
719 t
720 a
721 t
722 e
723  
724  
725  
726 1
727 1
728 4
729 8
730 6
731 4
732 0
733 .
734 0
735 

736 4
737  
738  
739  
740  
741  
742  
743  
744  
745  
746  
747  
748  
749  
750  
751  
752 J
753 o
754 n
755 a
756 s
757  
758 J
759 e
760 r
761 e
762 b
763 k
764 o
765  
766  
767  
768  
769  
770  
771  
772  
773  
774  
775 B
776 o
777 s
778 t
779 o
780 n
781  
782 C
783 e
784 l
785 t
786 i
787 c
788 s
789  
790  
791  
792  
793  
794  
795  
796 8
797  
798  
799  
800  
801  
802  
803  
804 P
805 F
806  
807  
808  
809 2
810 9
811  
812  
813 0
814 6
815 -
816 O
817 c
818 t
819  
820  
821  
822  
823  
824 2
825 3
826 1
827  
828  
829  
830  
831  
832  
833  
834  
835  
836  
837  
838  
839  
840  
841  
842  
843  
844  
845  
846  
847 N
848 a
849 N
850  
851  
852  
853 5
854 0
855 0
856 0
857 0
858 0
859 0
860 .
861 0
862 

863 5
864  
865  
866  
867  
868  
869  
870  
871  
872  
873  
874  
875  
876  
877  
878  
879  
880 A
881 m
882 i
883 r
884  
885 J
886 o
887 h
888 n
889 s
890 o
891 n
892  
893  
894  
895  
896  
897  
898  
899  
900  
901  
902 B
903 o
904 s
905 t
906 o
907 n
908  
909 C
910 e
911 l
912 t
913 i
914 c
915 s
916  
917  
918  
919  
920  
921  
922 9
923 0
924  
925  
926  
927  
928  
929  
930  
931 P
932 F
933  
934  
935  
936 2
937 9
938  
939  
940 0
941 6
942 -
943 S
944 e
945 p
946  
947  
948  
949  
950  
951 2
952 4
953 0
954  
955  
956  
957  
958  
959  
960  
961  
962  
963  
964  
965  
966  
967  
968  
969  
970  
971  
972  
973  
974 N
975 a
976 N
977  
978  
979 1
980 2
981 0
982 0
983 0
984 0
985 0
986 0
987 .
988 0
989 

990 6
991  
992  
993  
994  
995  
996  
997  
998  
999  
1000  
1001  
1002  
1003  
1004  
1005  
1006 J
1007 o
1008 r
1009 d
1010 a
1011 n
1012  
1013 M
1014 i
1015 c
1016 k
1017 e
1018 y
1019  
1020  
1021  
1022  
1023  
1024  
1025  
1026  
1027  
1028  
1029 B
1030 o
1031 s
1032 t
1033 o
1034 n
1035  
1036 C
1037 e
1038 l
1039 t
1040 i
1041 c
1042 s
1043  
1044  
1045  
1046  
1047  
1048  
1049 5
1050 5
1051  
1052  
1053  
1054  
1055  
1056  
1057  
1058 P
1059 F
1060  
1061  
1062  
1063 2
1064 1
1065  
1066  
1067 0
1068 6
1069 -
1070 A
1071 u
1072 g
1073  
1074  
1075  
1076  
1077  
1078 2
1079 3
1080 5
1081  
1082  
1083  
1084  
1085  
1086  
1087  
1088  
1089  
1090  
1091  
1092  
1093  
1094  
1095  
1096  
1097  
1098  
1099  
1100  
1101 L
1102 S
1103 U
1104  
1105  
1106  
1107 1
1108 1
1109 7
1110 0
1111 9
1112 6
1113 0
1114 .
1115 0
1116 

1117 7
1118  
1119  
1120  
1121  
1122  
1123  
1124  
1125  
1126  
1127  
1128  
1129  
1130  
1131  
1132  
1133  
1134 K
1135 e
1136 l
1137 l
1138 y
1139  
1140 O
1141 l
1142 y
1143 n
1144 y
1145 k
1146  
1147  
1148  
1149  
1150  
1151  
1152  
1153  
1154  
1155  
1156 B
1157 o
1158 s
1159 t
1160 o
1161 n
1162  
1163 C
1164 e
1165 l
1166 t
1167 i
1168 c
1169 s
1170  
1171  
1172  
1173  
1174  
1175  
1176 4
1177 1
1178  
1179  
1180  
1181  
1182  
1183  
1184  
1185  
1186 C
1187  
1188  
1189  
1190 2
1191 5
1192  
1193  
1194 J
1195 u
1196 l
1197 -
1198 0
1199 0
1200  
1201  
1202  
1203  
1204  
1205 2
1206 3
1207 8
1208  
1209  
1210  
1211  
1212  
1213  
1214  
1215  
1216  
1217  
1218  
1219  
1220  
1221  
1222  
1223  
1224 G
1225 o
1226 n
1227 z
1228 a
1229 g
1230 a
1231  
1232  
1233  
1234 2
1235 1
1236 6
1237 5
1238 1
1239 6
1240 0
1241 .
1242 0
1243 

1244 8
1245  
1246  
1247  
1248  
1249  
1250  
1251  
1252  
1253  
1254  
1255  
1256  
1257  
1258  
1259  
1260  
1261 T
1262 e
1263 r
1264 r
1265 y
1266  
1267 R
1268 o
1269 z
1270 i
1271 e
1272 r
1273  
1274  
1275  
1276  
1277  
1278  
1279  
1280  
1281  
1282  
1283 B
1284 o
1285 s
1286 t
1287 o
1288 n
1289  
1290 C
1291 e
1292 l
1293 t
1294 i
1295 c
1296 s
1297  
1298  
1299  
1300  
1301  
1302  
1303 1
1304 2
1305  
1306  
1307  
1308  
1309  
1310  
1311  
1312 P
1313 G
1314  
1315  
1316  
1317 2
1318 2
1319  
1320  
1321 0
1322 6
1323 -
1324 F
1325 e
1326 b
1327  
1328  
1329  
1330  
1331  
1332 1
1333 9
1334 0
1335  
1336  
1337  
1338  
1339  
1340  
1341  
1342  
1343  
1344  
1345  
1346  
1347  
1348 L
1349 o
1350 u
1351 i
1352 s
1353 v
1354 i
1355 l
1356 l
1357 e
1358  
1359  
1360  
1361 1
1362 8
1363 2
1364 4
1365 3
1366 6
1367 0
1368 .
1369 0
1370 

1371 9
1372  
1373  
1374  
1375  
1376  
1377  
1378  
1379  
1380  
1381  
1382  
1383  
1384  
1385  
1386  
1387  
1388 M
1389 a
1390 r
1391 c
1392 u
1393 s
1394  
1395 S
1396 m
1397 a
1398 r
1399 t
1400  
1401  
1402  
1403  
1404  
1405  
1406  
1407  
1408  
1409  
1410 B
1411 o
1412 s
1413 t
1414 o
1415 n
1416  
1417 C
1418 e
1419 l
1420 t
1421 i
1422 c
1423 s
1424  
1425  
1426  
1427  
1428  
1429  
1430 3
1431 6
1432  
1433  
1434  
1435  
1436  
1437  
1438  
1439 P
1440 G
1441  
1442  
1443  
1444 2
1445 2
1446  
1447  
1448 0
1449 6
1450 -
1451 A
1452 p
1453 r
1454  
1455  
1456  
1457  
1458  
1459 2
1460 2
1461 0
1462  
1463  
1464  
1465  
1466  
1467  
1468  
1469  
1470  
1471 O
1472 k
1473 l
1474 a
1475 h
1476 o
1477 m
1478 a
1479  
1480 S
1481 t
1482 a
1483 t
1484 e
1485  
1486  
1487  
1488 3
1489 4
1490 3
1491 1
1492 0
1493 4
1494 0
1495 .
1496 0
1497 

1498 1
1499 0
1500  
1501  
1502  
1503  
1504  
1505  
1506  
1507  
1508  
1509  
1510  
1511  
1512 J
1513 a
1514 r
1515 e
1516 d
1517  
1518 S
1519 u
1520 l
1521 l
1522 i
1523 n
1524 g
1525 e
1526 r
1527  
1528  
1529  
1530  
1531  
1532  
1533  
1534  
1535  
1536  
1537 B
1538 o
1539 s
1540 t
1541 o
1542 n
1543  
1544 C
1545 e
1546 l
1547 t
1548 i
1549 c
1550 s
1551  
1552  
1553  
1554  
1555  
1556  
1557  
1558 7
1559  
1560  
1561  
1562  
1563  
1564  
1565  
1566  
1567 C
1568  
1569  
1570  
1571 2
1572 4
1573  
1574  
1575 0
1576 6
1577 -
1578 S
1579 e
1580 p
1581  
1582  
1583  
1584  
1585  
1586 2
1587 6
1588 0
1589  
1590  
1591  
1592  
1593  
1594  
1595  
1596  
1597  
1598  
1599  
1600  
1601  
1602 O
1603 h
1604 i
1605 o
1606  
1607 S
1608 t
1609 a
1610 t
1611 e
1612  
1613  
1614  
1615 2
1616 5
1617 6
1618 9
1619 2
1620 6
1621 0
1622 .
1623 0
1624 

1625 1
1626 1
1627  
1628  
1629  
1630  
1631  
1632  
1633  
1634  
1635  
1636  
1637  
1638  
1639  
1640  
1641 I
1642 s
1643 a
1644 i
1645 a
1646 h
1647  
1648 T
1649 h
1650 o
1651 m
1652 a
1653 s
1654  
1655  
1656  
1657  
1658  
1659  
1660  
1661  
1662  
1663  
1664 B
1665 o
1666 s
1667 t
1668 o
1669 n
1670  
1671 C
1672 e
1673 l
1674 t
1675 i
1676 c
1677 s
1678  
1679  
1680  
1681  
1682  
1683  
1684  
1685 4
1686  
1687  
1688  
1689  
1690  
1691  
1692  
1693 P
1694 G
1695  
1696  
1697  
1698 2
1699 7
1700  
1701  
1702 0
1703 5
1704 -
1705 S
1706 e
1707 p
1708  
1709  
1710  
1711  
1712  
1713 1
1714 8
1715 5
1716  
1717  
1718  
1719  
1720  
1721  
1722  
1723  
1724  
1725  
1726  
1727  
1728  
1729 W
1730 a
1731 s
1732 h
1733 i
1734 n
1735 g
1736 t
1737 o
1738 n
1739  
1740  
1741  
1742 6
1743 9
1744 1
1745 2
1746 8
1747 6
1748 9
1749 .
1750 0
1751 

1752 1
1753 2
1754  
1755  
1756  
1757  
1758  
1759  
1760  
1761  
1762  
1763  
1764  
1765  
1766  
1767  
1768  
1769  
1770 E
1771 v
1772 a
1773 n
1774  
1775 T
1776 u
1777 r
1778 n
1779 e
1780 r
1781  
1782  
1783  
1784  
1785  
1786  
1787  
1788  
1789  
1790  
1791 B
1792 o
1793 s
1794 t
1795 o
1796 n
1797  
1798 C
1799 e
1800 l
1801 t
1802 i
1803 c
1804 s
1805  
1806  
1807  
1808  
1809  
1810  
1811 1
1812 1
1813  
1814  
1815  
1816  
1817  
1818  
1819  
1820 S
1821 G
1822  
1823  
1824  
1825 2
1826 7
1827  
1828  
1829 0
1830 6
1831 -
1832 J
1833 u
1834 l
1835  
1836  
1837  
1838  
1839  
1840 2
1841 2
1842 0
1843  
1844  
1845  
1846  
1847  
1848  
1849  
1850  
1851  
1852  
1853  
1854  
1855  
1856 O
1857 h
1858 i
1859 o
1860  
1861 S
1862 t
1863 a
1864 t
1865 e
1866  
1867  
1868  
1869 3
1870 4
1871 2
1872 5
1873 5
1874 1
1875 0
1876 .
1877 0
1878 

1879 1
1880 3
1881  
1882  
1883  
1884  
1885  
1886  
1887  
1888  
1889  
1890  
1891  
1892  
1893  
1894  
1895  
1896  
1897 J
1898 a
1899 m
1900 e
1901 s
1902  
1903 Y
1904 o
1905 u
1906 n
1907 g
1908  
1909  
1910  
1911  
1912  
1913  
1914  
1915  
1916  
1917  
1918 B
1919 o
1920 s
1921 t
1922 o
1923 n
1924  
1925 C
1926 e
1927 l
1928 t
1929 i
1930 c
1931 s
1932  
1933  
1934  
1935  
1936  
1937  
1938 1
1939 3
1940  
1941  
1942  
1943  
1944  
1945  
1946  
1947 S
1948 G
1949  
1950  
1951  
1952 2
1953 0
1954  
1955  
1956 0
1957 6
1958 -
1959 J
1960 u
1961 n
1962  
1963  
1964  
1965  
1966  
1967 2
1968 1
1969 5
1970  
1971  
1972  
1973  
1974  
1975  
1976  
1977  
1978  
1979  
1980  
1981  
1982  
1983  
1984  
1985 K
1986 e
1987 n
1988 t
1989 u
1990 c
1991 k
1992 y
1993  
1994  
1995  
1996 1
1997 7
1998 4
1999 9
2000 8
2001 4
2002 0
2003 .
2004 0
2005 

2006 1
2007 4
2008  
2009  
2010  
2011  
2012  
2013  
2014  
2015  
2016  
2017  
2018  
2019  
2020  
2021  
2022  
2023 T
2024 y
2025 l
2026 e
2027 r
2028  
2029 Z
2030 e
2031 l
2032 l
2033 e
2034 r
2035  
2036  
2037  
2038  
2039  
2040  
2041  
2042  
2043  
2044  
2045 B
2046 o
2047 s
2048 t
2049 o
2050 n
2051  
2052 C
2053 e
2054 l
2055 t
2056 i
2057 c
2058 s
2059  
2060  
2061  
2062  
2063  
2064  
2065 4
2066 4
2067  
2068  
2069  
2070  
2071  
2072  
2073  
2074  
2075 C
2076  
2077  
2078  
2079 2
2080 6
2081  
2082  
2083 J
2084 u
2085 l
2086 -
2087 0
2088 0
2089  
2090  
2091  
2092  
2093  
2094 2
2095 5
2096 3
2097  
2098  
2099  
2100  
2101  
2102  
2103  
2104  
2105  
2106 N
2107 o
2108 r
2109 t
2110 h
2111  
2112 C
2113 a
2114 r
2115 o
2116 l
2117 i
2118 n
2119 a
2120  
2121  
2122  
2123 2
2124 6
2125 1
2126 6
2127 9
2128 7
2129 5
2130 .
2131 0
2132 

2133 1
2134 5
2135  
2136  
2137  
2138  
2139  
2140  
2141  
2142  
2143  
2144  
2145  
2146 B
2147 o
2148 j
2149 a
2150 n
2151  
2152 B
2153 o
2154 g
2155 d
2156 a
2157 n
2158 o
2159 v
2160 i
2161 c
2162  
2163  
2164  
2165  
2166  
2167  
2168  
2169  
2170  
2171  
2172  
2173 B
2174 r
2175 o
2176 o
2177 k
2178 l
2179 y
2180 n
2181  
2182 N
2183 e
2184 t
2185 s
2186  
2187  
2188  
2189  
2190  
2191  
2192 4
2193 4
2194  
2195  
2196  
2197  
2198  
2199  
2200  
2201 S
2202 G
2203  
2204  
2205  
2206 2
2207 7
2208  
2209  
2210 0
2211 6
2212 -
2213 A
2214 u
2215 g
2216  
2217  
2218  
2219  
2220  
2221 2
2222 1
2223 6
2224  
2225  
2226  
2227  
2228  
2229  
2230  
2231  
2232  
2233  
2234  
2235  
2236  
2237  
2238  
2239  
2240  
2241  
2242  
2243  
2244 N
2245 a
2246 N
2247  
2248  
2249  
2250 3
2251 4
2252 2
2253 5
2254 5
2255 1
2256 0
2257 .
2258 0
2259 

2260 1
2261 6
2262  
2263  
2264  
2265  
2266  
2267  
2268  
2269  
2270  
2271  
2272  
2273  
2274  
2275  
2276  
2277 M
2278 a
2279 r
2280 k
2281 e
2282 l
2283  
2284 B
2285 r
2286 o
2287 w
2288 n
2289  
2290  
2291  
2292  
2293  
2294  
2295  
2296  
2297  
2298  
2299  
2300 B
2301 r
2302 o
2303 o
2304 k
2305 l
2306 y
2307 n
2308  
2309 N
2310 e
2311 t
2312 s
2313  
2314  
2315  
2316  
2317  
2318  
2319 2
2320 2
2321  
2322  
2323  
2324  
2325  
2326  
2327  
2328 S
2329 G
2330  
2331  
2332  
2333 2
2334 4
2335  
2336  
2337 0
2338 6
2339 -
2340 M
2341 a
2342 r
2343  
2344  
2345  
2346  
2347  
2348 1
2349 9
2350 0
2351  
2352  
2353  
2354  
2355  
2356  
2357  
2358  
2359  
2360 O
2361 k
2362 l
2363 a
2364 h
2365 o
2366 m
2367 a
2368  
2369 S
2370 t
2371 a
2372 t
2373 e
2374  
2375  
2376  
2377  
2378 8
2379 4
2380 5
2381 0
2382 5
2383 9
2384 .
2385 0
2386 

2387 1
2388 7
2389  
2390  
2391  
2392  
2393  
2394  
2395  
2396  
2397  
2398  
2399  
2400  
2401 W
2402 a
2403 y
2404 n
2405 e
2406  
2407 E
2408 l
2409 l
2410 i
2411 n
2412 g
2413 t
2414 o
2415 n
2416  
2417  
2418  
2419  
2420  
2421  
2422  
2423  
2424  
2425  
2426  
2427 B
2428 r
2429 o
2430 o
2431 k
2432 l
2433 y
2434 n
2435  
2436 N
2437 e
2438 t
2439 s
2440  
2441  
2442  
2443  
2444  
2445  
2446 2
2447 1
2448  
2449  
2450  
2451  
2452  
2453  
2454  
2455 S
2456 G
2457  
2458  
2459  
2460 2
2461 8
2462  
2463  
2464 0
2465 6
2466 -
2467 A
2468 p
2469 r
2470  
2471  
2472  
2473  
2474  
2475 2
2476 0
2477 0
2478  
2479  
2480  
2481  
2482  
2483  
2484  
2485  
2486  
2487 N
2488 o
2489 r
2490 t
2491 h
2492  
2493 C
2494 a
2495 r
2496 o
2497 l
2498 i
2499 n
2500 a
2501  
2502  
2503  
2504 1
2505 5
2506 0
2507 0
2508 0
2509 0
2510 0
2511 .
2512 0
2513 

2514 1
2515 8
2516  
2517  
2518  
2519  
2520 R
2521 o
2522 n
2523 d
2524 a
2525 e
2526  
2527 H
2528 o
2529 l
2530 l
2531 i
2532 s
2533 -
2534 J
2535 e
2536 f
2537 f
2538 e
2539 r
2540 s
2541 o
2542 n
2543  
2544  
2545  
2546  
2547  
2548  
2549  
2550  
2551  
2552  
2553  
2554 B
2555 r
2556 o
2557 o
2558 k
2559 l
2560 y
2561 n
2562  
2563 N
2564 e
2565 t
2566 s
2567  
2568  
2569  
2570  
2571  
2572  
2573 2
2574 4
2575  
2576  
2577  
2578  
2579  
2580  
2581  
2582 S
2583 G
2584  
2585  
2586  
2587 2
2588 1
2589  
2590  
2591 0
2592 6
2593 -
2594 J
2595 u
2596 l
2597  
2598  
2599  
2600  
2601  
2602 2
2603 2
2604 0
2605  
2606  
2607  
2608  
2609  
2610  
2611  
2612  
2613  
2614  
2615  
2616  
2617  
2618  
2619  
2620  
2621 A
2622 r
2623 i
2624 z
2625 o
2626 n
2627 a
2628  
2629  
2630  
2631 1
2632 3
2633 3
2634 5
2635 4
2636 8
2637 0
2638 .
2639 0
2640 

2641 1
2642 9
2643  
2644  
2645  
2646  
2647  
2648  
2649  
2650  
2651  
2652  
2653  
2654  
2655  
2656  
2657  
2658 J
2659 a
2660 r
2661 r
2662 e
2663 t
2664 t
2665  
2666 J
2667 a
2668 c
2669 k
2670  
2671  
2672  
2673  
2674  
2675  
2676  
2677  
2678  
2679  
2680  
2681 B
2682 r
2683 o
2684 o
2685 k
2686 l
2687 y
2688 n
2689  
2690 N
2691 e
2692 t
2693 s
2694  
2695  
2696  
2697  
2698  
2699  
2700  
2701 2
2702  
2703  
2704  
2705  
2706  
2707  
2708  
2709 P
2710 G
2711  
2712  
2713  
2714 3
2715 2
2716  
2717  
2718 0
2719 6
2720 -
2721 M
2722 a
2723 r
2724  
2725  
2726  
2727  
2728  
2729 2
2730 0
2731 0
2732  
2733  
2734  
2735  
2736  
2737  
2738  
2739  
2740  
2741  
2742  
2743 G
2744 e
2745 o
2746 r
2747 g
2748 i
2749 a
2750  
2751 T
2752 e
2753 c
2754 h
2755  
2756  
2757  
2758 6
2759 3
2760 0
2761 0
2762 0
2763 0
2764 0
2765 .
2766 0
2767 

2768 2
2769 0
2770  
2771  
2772  
2773  
2774  
2775  
2776  
2777  
2778  
2779  
2780  
2781  
2782  
2783 S
2784 e
2785 r
2786 g
2787 e
2788 y
2789  
2790 K
2791 a
2792 r
2793 a
2794 s
2795 e
2796 v
2797  
2798  
2799  
2800  
2801  
2802  
2803  
2804  
2805  
2806  
2807  
2808 B
2809 r
2810 o
2811 o
2812 k
2813 l
2814 y
2815 n
2816  
2817 N
2818 e
2819 t
2820 s
2821  
2822  
2823  
2824  
2825  
2826  
2827 1
2828 0
2829  
2830  
2831  
2832  
2833  
2834  
2835  
2836 S
2837 G
2838  
2839  
2840  
2841 2
2842 2
2843  
2844  
2845 0
2846 6
2847 -
2848 J
2849 u
2850 l
2851  
2852  
2853  
2854  
2855  
2856 2
2857 0
2858 8
2859  
2860  
2861  
2862  
2863  
2864  
2865  
2866  
2867  
2868  
2869  
2870  
2871  
2872  
2873  
2874  
2875  
2876  
2877  
2878  
2879 N
2880 a
2881 N
2882  
2883  
2884  
2885 1
2886 5
2887 9
2888 9
2889 8
2890 4
2891 0
2892 .
2893 0
2894 

2895 2
2896 1
2897  
2898  
2899  
2900  
2901  
2902  
2903  
2904  
2905  
2906  
2907  
2908  
2909 S
2910 e
2911 a
2912 n
2913  
2914 K
2915 i
2916 l
2917 p
2918 a
2919 t
2920 r
2921 i
2922 c
2923 k
2924  
2925  
2926  
2927  
2928  
2929  
2930  
2931  
2932  
2933  
2934  
2935 B
2936 r
2937 o
2938 o
2939 k
2940 l
2941 y
2942 n
2943  
2944 N
2945 e
2946 t
2947 s
2948  
2949  
2950  
2951  
2952  
2953  
2954  
2955 6
2956  
2957  
2958  
2959  
2960  
2961  
2962  
2963 S
2964 G
2965  
2966  
2967  
2968 2
2969 6
2970  
2971  
2972 0
2973 6
2974 -
2975 A
2976 p
2977 r
2978  
2979  
2980  
2981  
2982  
2983 2
2984 1
2985 9
2986  
2987  
2988  
2989  
2990  
2991  
2992  
2993  
2994  
2995  
2996  
2997  
2998  
2999 C
3000 i
3001 n
3002 c
3003 i
3004 n
3005 n
3006 a
3007 t
3008 i
3009  
3010  
3011  
3012  
3013 1
3014 3
3015 4
3016 2
3017 1
3018 5
3019 .
3020 0
3021 

3022 2
3023 2
3024  
3025  
3026  
3027  
3028  
3029  
3030  
3031  
3032  
3033  
3034  
3035  
3036  
3037  
3038  
3039 S
3040 h
3041 a
3042 n
3043 e
3044  
3045 L
3046 a
3047 r
3048 k
3049 i
3050 n
3051  
3052  
3053  
3054  
3055  
3056  
3057  
3058  
3059  
3060  
3061  
3062 B
3063 r
3064 o
3065 o
3066 k
3067 l
3068 y
3069 n
3070  
3071 N
3072 e
3073 t
3074 s
3075  
3076  
3077  
3078  
3079  
3080  
3081  
3082 0
3083  
3084  
3085  
3086  
3087  
3088  
3089  
3090 P
3091 G
3092  
3093  
3094  
3095 2
3096 3
3097  
3098  
3099 0
3100 5
3101 -
3102 N
3103 o
3104 v
3105  
3106  
3107  
3108  
3109  
3110 1
3111 7
3112 5
3113  
3114  
3115  
3116  
3117  
3118  
3119  
3120  
3121  
3122  
3123  
3124  
3125  
3126 M
3127 i
3128 a
3129 m
3130 i
3131  
3132 (
3133 F
3134 L
3135 )
3136  
3137  
3138  
3139 1
3140 5
3141 0
3142 0
3143 0
3144 0
3145 0
3146 .
3147 0
3148 

3149 2
3150 3
3151  
3152  
3153  
3154  
3155  
3156  
3157  
3158  
3159  
3160  
3161  
3162  
3163  
3164  
3165  
3166  
3167 B
3168 r
3169 o
3170 o
3171 k
3172  
3173 L
3174 o
3175 p
3176 e
3177 z
3178  
3179  
3180  
3181  
3182  
3183  
3184  
3185  
3186  
3187  
3188  
3189 B
3190 r
3191 o
3192 o
3193 k
3194 l
3195 y
3196 n
3197  
3198 N
3199 e
3200 t
3201 s
3202  
3203  
3204  
3205  
3206  
3207  
3208 1
3209 1
3210  
3211  
3212  
3213  
3214  
3215  
3216  
3217  
3218 C
3219  
3220  
3221  
3222 2
3223 8
3224  
3225  
3226 J
3227 u
3228 l
3229 -
3230 0
3231 0
3232  
3233  
3234  
3235  
3236  
3237 2
3238 7
3239 5
3240  
3241  
3242  
3243  
3244   
3245  
3246  
3247  
3248  
3249  
3250  
3251  
3252  
3253  
3254  
3255 S
3256 t
3257 a
3258 n
3259 f
3260 o
3261 r
3262 d
3263  
3264  
3265 1
3266 9
3267 6
3268 8
3269 9
3270 0
3271 0
3272 0
3273 .
3274 0
3275 

3276 2
3277 4
3278  
3279  
3280  
3281  
3282  
3283  
3284  
3285  
3286  
3287  
3288  
3289 C
3290 h
3291 r
3292 i
3293 s
3294  
3295 M
3296 c
3297 C
3298 u
3299 l
3300 l
3301 o
3302 u
3303 g
3304 h
3305  
3306  
3307  
3308  
3309  
3310  
3311  
3312  
3313  
3314  
3315  
3316 B
3317 r
3318 o
3319 o
3320 k
3321 l
3322 y
3323 n
3324  
3325 N
 3326 e
3327 t
3328 s
3329  
3330  
3331  
3332  
3333  
3334  
3335  
3336 1
3337  
3338  
3339  
3340  
3341  
3342  
3343  
3344 P
3345 F
3346  
3347  
3348  
3349 2
3350 1
3351  
3352  
3353 0
3354 6
3355 -
3356 N
3357 o
3358 v
3359  
3360  
3361  
3362  
3363  
3364 2
3365 0
3366 0
3367  
3368  
3369  
3370  
3371  
3372  
3373  
3374  
3375  
3376  
3377  
3378  
3379  
3380  
3381  
3382 S
3383 y
3384 r
3385 a
3386 c
3387 u
3388 s
3389 e
3390  
3391  
3392  
3393 1
3394 1
3395 4
3396 0
3397 2
3398 4
3399 0
3400 .
3401 0
3402 

3403 2
3404 5
3405  
3406  
3407  
3408  
3409  
3410  
3411  
3412  
3413  
3414  
3415  
3416  
3417  
3418  
3419  
3420  
3421 W
3422 i
3423 l
3424 l
3425 i
3426 e
3427  
3428 R
3429 e
3430 e
3431 d
3432  
3433  
3434  
3435  
3436  
3437  
3438  
3439  
3440  
3441  
3442  
3443 B
3444 r
3445 o
3446 o
3447 k
3448 l
3449 y
3450 n
3451  
3452 N
3453 e
3454 t
3455 s
3456  
3457  
3458  
3459  
3460  
3461  
3462 3
3463 3
3464  
3465  
3466  
3467  
3468  
3469  
3470  
3471 P
3472 F
3473  
3474  
3475  
3476 2
3477 6
3478  
3479  
3480 0
3481 6
3482 -
3483 O
3484 c
3485 t
3486  
3487  
3488  
3489  
3490  
3491 2
3492 2
3493 0
3494  
3495  
3496  
3497  
3498  
3499  
3500  
3501  
3502  
3503  
3504  
3505  
3506 STraceback (most recent call last):
  File "<pyshell#45>", line 2, in <module>
    print(i,j)
KeyboardInterrupt
>>> for i in enumerate(d)
SyntaxError: invalid syntax
>>> for i in enumerate(d):
	print(i)

	
(0, ' ')
(1, ' ')
(2, ' ')
(3, ' ')
(4, ' ')
(5, ' ')
(6, ' ')
(7, ' ')
(8, ' ')
(9, ' ')
(10, ' ')
(11, ' ')
(12, ' ')
(13, ' ')
(14, ' ')
(15, ' ')
(16, ' ')
(17, ' ')
(18, ' ')
(19, ' ')
(20, ' ')
(21, ' ')
(22, ' ')
(23, ' ')
(24, ' ')
(25, 'N')
(26, 'a')
(27, 'm')
(28, 'e')
(29, ' ')
(30, ' ')
(31, ' ')
(32, ' ')
(33, ' ')
(34, ' ')
(35, ' ')
(36, ' ')
(37, ' ')
(38, ' ')
(39, ' ')
(40, ' ')
(41, ' ')
(42, ' ')
(43, ' ')
(44, ' ')
(45, ' ')
(46, ' ')
(47, ' ')
(48, ' ')
(49, 'T')
(50, 'e')
(51, 'a')
(52, 'm')
(53, ' ')
(54, ' ')
(55, 'N')
(56, 'u')
(57, 'm')
(58, 'b')
(59, 'e')
(60, 'r')
(61, ' ')
(62, 'P')
(63, 'o')
(64, 's')
(65, 'i')
(66, 't')
(67, 'i')
(68, 'o')
(69, 'n')
(70, ' ')
(71, ' ')
(72, 'A')
(73, 'g')
(74, 'e')
(75, ' ')
(76, ' ')
(77, 'H')
(78, 'e')
(79, 'i')
(80, 'g')
(81, 'h')
(82, 't')
(83, ' ')
(84, ' ')
(85, 'W')
(86, 'e')
(87, 'i')
(88, 'g')
(89, 'h')
(90, 't')
(91, ' ')
(92, ' ')
(93, ' ')
(94, ' ')
(95, ' ')
(96, ' ')
(97, ' ')
(98, ' ')
(99, ' ')
(100, ' ')
(101, ' ')
(102, ' ')
(103, ' ')
(104, ' ')
(105, ' ')
(106, ' ')
(107, 'C')
(108, 'o')
(109, 'l')
(110, 'l')
(111, 'e')
(112, 'g')
(113, 'e')
(114, ' ')
(115, ' ')
(116, ' ')
(117, ' ')
(118, ' ')
(119, ' ')
(120, 'S')
(121, 'a')
(122, 'l')
(123, 'a')
(124, 'r')
(125, 'y')
(126, '\n')
(127, '0')
(128, ' ')
(129, ' ')
(130, ' ')
(131, ' ')
(132, ' ')
(133, ' ')
(134, ' ')
(135, ' ')
(136, ' ')
(137, ' ')
(138, ' ')
(139, ' ')
(140, ' ')
(141, ' ')
(142, ' ')
(143, 'A')
(144, 'v')
(145, 'e')
(146, 'r')
(147, 'y')
(148, ' ')
(149, 'B')
(150, 'r')
(151, 'a')
(152, 'd')
(153, 'l')
(154, 'e')
(155, 'y')
(156, ' ')
(157, ' ')
(158, ' ')
(159, ' ')
(160, ' ')
(161, ' ')
(162, ' ')
(163, ' ')
(164, ' ')
(165, ' ')
(166, 'B')
(167, 'o')
(168, 's')
(169, 't')
(170, 'o')
(171, 'n')
(172, ' ')
(173, 'C')
(174, 'e')
(175, 'l')
(176, 't')
(177, 'i')
(178, 'c')
(179, 's')
(180, ' ')
(181, ' ')
(182, ' ')
(183, ' ')
(184, ' ')
(185, ' ')
(186, ' ')
(187, '0')
(188, ' ')
(189, ' ')
(190, ' ')
(191, ' ')
(192, ' ')
(193, ' ')
(194, ' ')
(195, 'P')
(196, 'G')
(197, ' ')
(198, ' ')
(199, ' ')
(200, '2')
(201, '5')
(202, ' ')
(203, ' ')
(204, '0')
(205, '6')
(206, '-')
(207, 'F')
(208, 'e')
(209, 'b')
(210, ' ')
(211, ' ')
(212, ' ')
(213, ' ')
(214, ' ')
(215, '1')
(216, '8')
(217, '0')
(218, ' ')
(219, ' ')
(220, ' ')
(221, ' ')
(222, ' ')
(223, ' ')
(224, ' ')
(225, ' ')
(226, ' ')
(227, ' ')
(228, ' ')
(229, ' ')
(230, ' ')
(231, ' ')
(232, ' ')
(233, ' ')
(234, ' ')
(235, ' ')
(236, 'T')
(237, 'e')
(238, 'x')
(239, 'a')
(240, 's')
(241, ' ')
(242, ' ')
(243, ' ')
(244, '7')
(245, '7')
(246, '3')
(247, '0')
(248, '3')
(249, '3')
(250, '7')
(251, '.')
(252, '0')
(253, '\n')
(254, '1')
(255, ' ')
(256, ' ')
(257, ' ')
(258, ' ')
(259, ' ')
(260, ' ')
(261, ' ')
(262, ' ')
(263, ' ')
(264, ' ')
(265, ' ')
(266, ' ')
(267, ' ')
(268, ' ')
(269, ' ')
(270, ' ')
(271, ' ')
(272, 'J')
(273, 'a')
(274, 'e')
(275, ' ')
(276, 'C')
(277, 'r')
(278, 'o')
(279, 'w')
(280, 'd')
(281, 'e')
(282, 'r')
(283, ' ')
(284, ' ')
(285, ' ')
(286, ' ')
(287, ' ')
(288, ' ')
(289, ' ')
(290, ' ')
(291, ' ')
(292, ' ')
(293, 'B')
(294, 'o')
(295, 's')
(296, 't')
(297, 'o')
(298, 'n')
(299, ' ')
(300, 'C')
(301, 'e')
(302, 'l')
(303, 't')
(304, 'i')
(305, 'c')
(306, 's')
(307, ' ')
(308, ' ')
(309, ' ')
(310, ' ')
(311, ' ')
(312, ' ')
(313, '9')
(314, '9')
(315, ' ')
(316, ' ')
(317, ' ')
(318, ' ')
(319, ' ')
(320, ' ')
(321, ' ')
(322, 'S')
(323, 'F')
(324, ' ')
(325, ' ')
(326, ' ')
(327, '2')
(328, '5')
(329, ' ')
(330, ' ')
(331, '0')
(332, '6')
(333, '-')
(334, 'J')
(335, 'u')
(336, 'n')
(337, ' ')
(338, ' ')
(339, ' ')
(340, ' ')
(341, ' ')
(342, '2')
(343, '3')
(344, '5')
(345, ' ')
(346, ' ')
(347, ' ')
(348, ' ')
(349, ' ')
(350, ' ')
(351, ' ')
(352, ' ')
(353, ' ')
(354, ' ')
(355, ' ')
(356, ' ')
(357, ' ')
(358, ' ')
(359, 'M')
(360, 'a')
(361, 'r')
(362, 'q')
(363, 'u')
(364, 'e')
(365, 't')
(366, 't')
(367, 'e')
(368, ' ')
(369, ' ')
(370, ' ')
(371, '6')
(372, '7')
(373, '9')
(374, '6')
(375, '1')
(376, '1')
(377, '7')
(378, '.')
(379, '0')
(380, '\n')
(381, '2')
(382, ' ')
(383, ' ')
(384, ' ')
(385, ' ')
(386, ' ')
(387, ' ')
(388, ' ')
(389, ' ')
(390, ' ')
(391, ' ')
(392, ' ')
(393, ' ')
(394, ' ')
(395, ' ')
(396, ' ')
(397, ' ')
(398, 'J')
(399, 'o')
(400, 'h')
(401, 'n')
(402, ' ')
(403, 'H')
(404, 'o')
(405, 'l')
(406, 'l')
(407, 'a')
(408, 'n')
(409, 'd')
(410, ' ')
(411, ' ')
(412, ' ')
(413, ' ')
(414, ' ')
(415, ' ')
(416, ' ')
(417, ' ')
(418, ' ')
(419, ' ')
(420, 'B')
(421, 'o')
(422, 's')
(423, 't')
(424, 'o')
(425, 'n')
(426, ' ')
(427, 'C')
(428, 'e')
(429, 'l')
(430, 't')
(431, 'i')
(432, 'c')
(433, 's')
(434, ' ')
(435, ' ')
(436, ' ')
(437, ' ')
(438, ' ')
(439, ' ')
(440, '3')
(441, '0')
(442, ' ')
(443, ' ')
(444, ' ')
(445, ' ')
(446, ' ')
(447, ' ')
(448, ' ')
(449, 'S')
(450, 'G')
(451, ' ')
(452, ' ')
(453, ' ')
(454, '2')
(455, '7')
(456, ' ')
(457, ' ')
(458, '0')
(459, '6')
(460, '-')
(461, 'M')
(462, 'a')
(463, 'y')
(464, ' ')
(465, ' ')
(466, ' ')
(467, ' ')
(468, ' ')
(469, '2')
(470, '0')
(471, '5')
(472, ' ')
(473, ' ')
(474, ' ')
(475, ' ')
(476, ' ')
(477, ' ')
(478, 'B')
(479, 'o')
(480, 's')
(481, 't')
(482, 'o')
(483, 'n')
(484, ' ')
(485, 'U')
(486, 'n')
(487, 'i')
(488, 'v')
(489, 'e')
(490, 'r')
(491, 's')
(492, 'i')
(493, 't')
(494, 'y')
(495, ' ')
(496, ' ')
(497, ' ')
(498, ' ')
(499, ' ')
(500, ' ')
(501, ' ')
(502, ' ')
(503, ' ')
(504, 'N')
(505, 'a')
(506, 'N')
(507, '\n')
(508, '3')
(509, ' ')
(510, ' ')
(511, ' ')
(512, ' ')
(513, ' ')
(514, ' ')
(515, ' ')
(516, ' ')
(517, ' ')
(518, ' ')
(519, ' ')
(520, ' ')
(521, ' ')
(522, ' ')
(523, ' ')
(524, ' ')
(525, ' ')
(526, 'R')
(527, '.')
(528, 'J')
(529, '.')
(530, ' ')
(531, 'H')
(532, 'u')
(533, 'n')
(534, 't')
(535, 'e')
(536, 'r')
(537, ' ')
(538, ' ')
(539, ' ')
(540, ' ')
(541, ' ')
(542, ' ')
(543, ' ')
(544, ' ')
(545, ' ')
(546, ' ')
(547, 'B')
(548, 'o')
(549, 's')
(550, 't')
(551, 'o')
(552, 'n')
(553, ' ')
(554, 'C')
(555, 'e')
(556, 'l')
(557, 't')
(558, 'i')
(559, 'c')
(560, 's')
(561, ' ')
(562, ' ')
(563, ' ')
(564, ' ')
(565, ' ')
(566, ' ')
(567, '2')
(568, '8')
(569, ' ')
(570, ' ')
(571, ' ')
(572, ' ')
(573, ' ')
(574, ' ')
(575, ' ')
(576, 'S')
(577, 'G')
(578, ' ')
(579, ' ')
(580, ' ')
(581, '2')
(582, '2')
(583, ' ')
(584, ' ')
(585, '0')
(586, '6')
(587, '-')
(588, 'M')
(589, 'a')
(590, 'y')
(591, ' ')
(592, ' ')
(593, ' ')
(594, ' ')
(595, ' ')
(596, '1')
(597, '8')
(598, '5')
(599, ' ')
(600, ' ')
(601, ' ')
(602, ' ')
(603, ' ')
(604, ' ')
(605, ' ')
(606, ' ')
(607, ' ')
(608, ' ')
(609, 'G')
(610, 'e')
(611, 'o')
(612, 'r')
(613, 'g')
(614, 'i')
(615, 'a')
(616, ' ')
(617, 'S')
(618, 't')
(619, 'a')
(620, 't')
(621, 'e')
(622, ' ')
(623, ' ')
(624, ' ')
(625, '1')
(626, '1')
(627, '4')
(628, '8')
(629, '6')
(630, '4')
(631, '0')
(632, '.')
(633, '0')
(634, '\n')
(635, '4')
(636, ' ')
(637, ' ')
(638, ' ')
(639, ' ')
(640, ' ')
(641, ' ')
(642, ' ')
(643, ' ')
(644, ' ')
(645, ' ')
(646, ' ')
(647, ' ')
(648, ' ')
(649, ' ')
(650, ' ')
(651, 'J')
(652, 'o')
(653, 'n')
(654, 'a')
(655, 's')
(656, ' ')
(657, 'J')
(658, 'e')
(659, 'r')
(660, 'e')
(661, 'b')
(662, 'k')
(663, 'o')
(664, ' ')
(665, ' ')
(666, ' ')
(667, ' ')
(668, ' ')
(669, ' ')
(670, ' ')
(671, ' ')
(672, ' ')
(673, ' ')
(674, 'B')
(675, 'o')
(676, 's')
(677, 't')
(678, 'o')
(679, 'n')
(680, ' ')
(681, 'C')
(682, 'e')
(683, 'l')
(684, 't')
(685, 'i')
(686, 'c')
(687, 's')
(688, ' ')
(689, ' ')
(690, ' ')
(691, ' ')
(692, ' ')
(693, ' ')
(694, ' ')
(695, '8')
(696, ' ')
(697, ' ')
(698, ' ')
(699, ' ')
(700, ' ')
(701, ' ')
(702, ' ')
(703, 'P')
(704, 'F')
(705, ' ')
(706, ' ')
(707, ' ')
(708, '2')
(709, '9')
(710, ' ')
(711, ' ')
(712, '0')
(713, '6')
(714, '-')
(715, 'O')
(716, 'c')
(717, 't')
(718, ' ')
(719, ' ')
(720, ' ')
(721, ' ')
(722, ' ')
(723, '2')
(724, '3')
(725, '1')
(726, ' ')
(727, ' ')
(728, ' ')
(729, ' ')
(730, ' ')
(731, ' ')
(732, ' ')
(733, ' ')
(734, ' ')
(735, ' ')
(736, ' ')
(737, ' ')
(738, ' ')
(739, ' ')
(740, ' ')
(741, ' ')
(742, ' ')
(743, ' ')
(744, ' ')
(745, ' ')
(746, 'N')
(747, 'a')
(748, 'N')
(749, ' ')
(750, ' ')
(751, ' ')
(752, '5')
(753, '0')
(754, '0')
(755, '0')
(756, '0')
(757, '0')
(758, '0')
(759, '.')
(760, '0')
(761, '\n')
(762, '5')
(763, ' ')
(764, ' ')
(765, ' ')
(766, ' ')
(767, ' ')
(768, ' ')
(769, ' ')
(770, ' ')
(771, ' ')
(772, ' ')
(773, ' ')
(774, ' ')
(775, ' ')
(776, ' ')
(777, ' ')
(778, ' ')
(779, 'A')
(780, 'm')
(781, 'i')
(782, 'r')
(783, ' ')
(784, 'J')
(785, 'o')
(786, 'h')
(787, 'n')
(788, 's')
(789, 'o')
(790, 'n')
(791, ' ')
(792, ' ')
(793, ' ')
(794, ' ')
(795, ' ')
(796, ' ')
(797, ' ')
(798, ' ')
(799, ' ')
(800, ' ')
(801, 'B')
(802, 'o')
(803, 's')
(804, 't')
(805, 'o')
(806, 'n')
(807, ' ')
(808, 'C')
(809, 'e')
(810, 'l')
(811, 't')
(812, 'i')
(813, 'c')
(814, 's')
(815, ' ')
(816, ' ')
(817, ' ')
(818, ' ')
(819, ' ')
(820, ' ')
(821, '9')
(822, '0')
(823, ' ')
(824, ' ')
(825, ' ')
(826, ' ')
(827, ' ')
(828, ' ')
(829, ' ')
(830, 'P')
(831, 'F')
(832, ' ')
(833, ' ')
(834, ' ')
(835, '2')
(836, '9')
(837, ' ')
(838, ' ')
(839, '0')
(840, '6')
(841, '-')
(842, 'S')
(843, 'e')
(844, 'p')
(845, ' ')
(846, ' ')
(847, ' ')
(848, ' ')
(849, ' ')
(850, '2')
(851, '4')
(852, '0')
(853, ' ')
(854, ' ')
(855, ' ')
(856, ' ')
(857, ' ')
(858, ' ')
(859, ' ')
(860, ' ')
(861, ' ')
(862, ' ')
(863, ' ')
(864, ' ')
(865, ' ')
(866, ' ')
(867, ' ')
(868, ' ')
(869, ' ')
(870, ' ')
(871, ' ')
(872, ' ')
(873, 'N')
(874, 'a')
(875, 'N')
(876, ' ')
(877, ' ')
(878, '1')
(879, '2')
(880, '0')
(881, '0')
(882, '0')
(883, '0')
(884, '0')
(885, '0')
(886, '.')
(887, '0')
(888, '\n')
(889, '6')
(890, ' ')
(891, ' ')
(892, ' ')
(893, ' ')
(894, ' ')
(895, ' ')
(896, ' ')
(897, ' ')
(898, ' ')
(899, ' ')
(900, ' ')
(901, ' ')
(902, ' ')
(903, ' ')
(904, ' ')
(905, 'J')
(906, 'o')
(907, 'r')
(908, 'd')
(909, 'a')
(910, 'n')
(911, ' ')
(912, 'M')
(913, 'i')
(914, 'c')
(915, 'k')
(916, 'e')
(917, 'y')
(918, ' ')
(919, ' ')
(920, ' ')
(921, ' ')
(922, ' ')
(923, ' ')
(924, ' ')
(925, ' ')
(926, ' ')
(927, ' ')
(928, 'B')
(929, 'o')
(930, 's')
(931, 't')
(932, 'o')
(933, 'n')
(934, ' ')
(935, 'C')
(936, 'e')
(937, 'l')
(938, 't')
(939, 'i')
(940, 'c')
(941, 's')
(942, ' ')
(943, ' ')
(944, ' ')
(945, ' ')
(946, ' ')
(947, ' ')
(948, '5')
(949, '5')
(950, ' ')
(951, ' ')
(952, ' ')
(953, ' ')
(954, ' ')
(955, ' ')
(956, ' ')
(957, 'P')
(958, 'F')
(959, ' ')
(960, ' ')
(961, ' ')
(962, '2')
(963, '1')
(964, ' ')
(965, ' ')
(966, '0')
(967, '6')
(968, '-')
(969, 'A')
(970, 'u')
(971, 'g')
(972, ' ')
(973, ' ')
(974, ' ')
(975, ' ')
(976, ' ')
(977, '2')
(978, '3')
(979, '5')
(980, ' ')
(981, ' ')
(982, ' ')
(983, ' ')
(984, ' ')
(985, ' ')
(986, ' ')
(987, ' ')
(988, ' ')
(989, ' ')
(990, ' ')
(991, ' ')
(992, ' ')
(993, ' ')
(994, ' ')
(995, ' ')
(996, ' ')
(997, ' ')
(998, ' ')
(999, ' ')
(1000, 'L')
(1001, 'S')
(1002, 'U')
(1003, ' ')
(1004, ' ')
(1005, ' ')
(1006, '1')
(1007, '1')
(1008, '7')
(1009, '0')
(1010, '9')
(1011, '6')
(1012, '0')
(1013, '.')
(1014, '0')
(1015, '\n')
(1016, '7')
(1017, ' ')
(1018, ' ')
(1019, ' ')
(1020, ' ')
(1021, ' ')
(1022, ' ')
(1023, ' ')
(1024, ' ')
(1025, ' ')
(1026, ' ')
(1027, ' ')
(1028, ' ')
(1029, ' ')
(1030, ' ')
(1031, ' ')
(1032, ' ')
(1033, 'K')
(1034, 'e')
(1035, 'l')
(1036, 'l')
(1037, 'y')
(1038, ' ')
(1039, 'O')
(1040, 'l')
(1041, 'y')
(1042, 'n')
(1043, 'y')
(1044, 'k')
(1045, ' ')
(1046, ' ')
(1047, ' ')
(1048, ' ')
(1049, ' ')
(1050, ' ')
(1051, ' ')
(1052, ' ')
(1053, ' ')
(1054, ' ')
(1055, 'B')
(1056, 'o')
(1057, 's')
(1058, 't')
(1059, 'o')
(1060, 'n')
(1061, ' ')
(1062, 'C')
(1063, 'e')
(1064, 'l')
(1065, 't')
(1066, 'i')
(1067, 'c')
(1068, 's')
(1069, ' ')
(1070, ' ')
(1071, ' ')
(1072, ' ')
(1073, ' ')
(1074, ' ')
(1075, '4')
(1076, '1')
(1077, ' ')
(1078, ' ')
(1079, ' ')
(1080, ' ')
(1081, ' ')
(1082, ' ')
(1083, ' ')
(1084, ' ')
(1085, 'C')
(1086, ' ')
(1087, ' ')
(1088, ' ')
(1089, '2')
(1090, '5')
(1091, ' ')
(1092, ' ')
(1093, 'J')
(1094, 'u')
(1095, 'l')
(1096, '-')
(1097, '0')
(1098, '0')
(1099, ' ')
(1100, ' ')
(1101, ' ')
(1102, ' ')
(1103, ' ')
(1104, '2')
(1105, '3')
(1106, '8')
(1107, ' ')
(1108, ' ')
(1109, ' ')
(1110, ' ')
(1111, ' ')
(1112, ' ')
(1113, ' ')
(1114, ' ')
(1115, ' ')
(1116, ' ')
(1117, ' ')
(1118, ' ')
(1119, ' ')
(1120, ' ')
(1121, ' ')
(1122, ' ')
(1123, 'G')
(1124, 'o')
(1125, 'n')
(1126, 'z')
(1127, 'a')
(1128, 'g')
(1129, 'a')
(1130, ' ')
(1131, ' ')
(1132, ' ')
(1133, '2')
(1134, '1')
(1135, '6')
(1136, '5')Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    print(i)
KeyboardInterrupt
>>> 