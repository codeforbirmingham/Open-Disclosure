angular.module('openDisclosure')
    .controller('homeCtrl', function ($scope, $http, $rootScope, $location) {

        $scope.candidates = sampleData;
        
        //This is bad.  Let's maybe give the side bar its own controller
        $rootScope.candidates = sampleData;

        $scope.totals = {
            contributions: 0,
            expenditures: 0,
            count: 0
        };

        for (var i in $scope.candidates) {
            $scope.totals.contributions += parseInt($scope.candidates[i].contributions);
            $scope.totals.expenditures += parseInt($scope.candidates[i].expenditures);
            $scope.totals.count += parseInt($scope.candidates[i].count);
        }

        $scope.candidatesDisplayed = 10;

        $scope.showMore = function () {
            $scope.candidatesDisplayed += 10;
        };

    });

var sampleData = [
    {
        "name": "ROBERT BENTLEY",
        "expenditures": 2197745,
        "contributions": 3214418,
        "count": 1687
  },
    {
        "name": "JOSEPH LISTER HUBBARD JR.",
        "expenditures": 353750,
        "contributions": 1209348,
        "count": 106
  },
    {
        "name": "LUTHER J. STRANGE III",
        "expenditures": 954421,
        "contributions": 1093742,
        "count": 889
  },
    {
        "name": "MICHAEL G. HUBBARD",
        "expenditures": 985085,
        "contributions": 887603,
        "count": 322
  },
    {
        "name": "CHRIS \"CHIP\" BEEKER JR.",
        "expenditures": 606950,
        "contributions": 585259,
        "count": 216
  },
    {
        "name": "DEL MARSH",
        "expenditures": 641893,
        "contributions": 574261,
        "count": 186
  },
    {
        "name": "CLYDE CHAMBLISS JR.",
        "expenditures": 494663,
        "contributions": 533951,
        "count": 492
  },
    {
        "name": "TOM WHATLEY",
        "expenditures": 599957,
        "contributions": 492515,
        "count": 235
  },
    {
        "name": "GERALD DIAL",
        "expenditures": 467908,
        "contributions": 485261,
        "count": 159
  },
    {
        "name": "JEREMY H. ODEN",
        "expenditures": 462577,
        "contributions": 482990,
        "count": 146
  },
    {
        "name": "JIMMY W. HOLLEY",
        "expenditures": 341233,
        "contributions": 459236,
        "count": 272
  },
    {
        "name": "MARVIN MCDANIEL BUTTRAM",
        "expenditures": 289135,
        "contributions": 453107,
        "count": 202
  },
    {
        "name": "SHAY WESLEY SHELNUTT",
        "expenditures": 339179,
        "contributions": 452426,
        "count": 172
  },
    {
        "name": "KAY E. IVEY",
        "expenditures": 635166,
        "contributions": 424847,
        "count": 751
  },
    {
        "name": "STANLEY KYLE COOKE",
        "expenditures": 434757,
        "contributions": 424400,
        "count": 88
  },
    {
        "name": "JACK WILLIAMS",
        "expenditures": 415820,
        "contributions": 416890,
        "count": 227
  },
    {
        "name": "PARKER GRIFFITH",
        "expenditures": 377495,
        "contributions": 404366,
        "count": 122
  },
    {
        "name": "PAUL HARRIS GARNER",
        "expenditures": 378710,
        "contributions": 403068,
        "count": 207
  },
    {
        "name": "TIMOTHY IVAN MELSON",
        "expenditures": 313574,
        "contributions": 400186,
        "count": 184
  },
    {
        "name": "REESE HOWELL MCKINNEY JR.",
        "expenditures": 383041,
        "contributions": 362072,
        "count": 661
  },
    {
        "name": "STEVE FLOWERS",
        "expenditures": 295433,
        "contributions": 346162,
        "count": 15
  },
    {
        "name": "WILLIAM TAYLOR STEWART",
        "expenditures": 195931,
        "contributions": 337671,
        "count": 63
  },
    {
        "name": "STEVE LIVINGSTON",
        "expenditures": 264762,
        "contributions": 332308,
        "count": 139
  },
    {
        "name": "FELIX BARRY MOORE",
        "expenditures": 300855,
        "contributions": 311786,
        "count": 97
  },
    {
        "name": "ROGER H BEDFORD JR.",
        "expenditures": 227415,
        "contributions": 289471,
        "count": 154
  },
    {
        "name": "FRED S TOOMER II",
        "expenditures": 282988,
        "contributions": 283731,
        "count": 36
  },
    {
        "name": "BRETT ASHLEY KING",
        "expenditures": 182338,
        "contributions": 280913,
        "count": 229
  },
    {
        "name": "PAUL BUSSMAN",
        "expenditures": 198674,
        "contributions": 279728,
        "count": 124
  },
    {
        "name": "GERALD ALLEN",
        "expenditures": 234022,
        "contributions": 277789,
        "count": 119
  },
    {
        "name": "MACK NEWMAN BUTLER",
        "expenditures": 209080,
        "contributions": 270732,
        "count": 121
  },
    {
        "name": "JIM H MCCLENDON",
        "expenditures": 377247,
        "contributions": 257789,
        "count": 120
  },
    {
        "name": "JOHN H MERRILL",
        "expenditures": 436351,
        "contributions": 245475,
        "count": 551
  },
    {
        "name": "TODD GREESON",
        "expenditures": 176807,
        "contributions": 225724,
        "count": 41
  },
    {
        "name": "JERRY L FIELDING",
        "expenditures": 258449,
        "contributions": 224636,
        "count": 91
  },
    {
        "name": "HARRI ANNE SMITH",
        "expenditures": 235814,
        "contributions": 208746,
        "count": 47
  },
    {
        "name": "WILLIAM L HOLTZCLAW",
        "expenditures": 184862,
        "contributions": 208289,
        "count": 104
  },
    {
        "name": "WILLIAM GARRETH MOORE",
        "expenditures": 344524,
        "contributions": 200830,
        "count": 13
  },
    {
        "name": "ARNOLD G MOONEY II",
        "expenditures": 198371,
        "contributions": 199868,
        "count": 229
  },
    {
        "name": "PAUL SANFORD",
        "expenditures": 130780,
        "contributions": 198342,
        "count": 171
  },
    {
        "name": "STEVEN DUANE GUEDE",
        "expenditures": 63344,
        "contributions": 191799,
        "count": 68
  },
    {
        "name": "AUBREY KURT WALLACE",
        "expenditures": 129663,
        "contributions": 190960,
        "count": 87
  },
    {
        "name": "CHRIS SELLS",
        "expenditures": 123848,
        "contributions": 190052,
        "count": 120
  },
    {
        "name": "WILLIAM E HENRY",
        "expenditures": 168765,
        "contributions": 187797,
        "count": 142
  },
    {
        "name": "WILLIAM ALFRED ROBERTS",
        "expenditures": 116614,
        "contributions": 187522,
        "count": 90
  },
    {
        "name": "GREGORY LAMAR ALBRITTON",
        "expenditures": 128422,
        "contributions": 184252,
        "count": 91
  },
    {
        "name": "JAMES T WAGGONER JR.",
        "expenditures": 25287,
        "contributions": 180319,
        "count": 80
  },
    {
        "name": "PHILLIP WAYNE WILLIAMS JR.",
        "expenditures": 116842,
        "contributions": 179909,
        "count": 86
  },
    {
        "name": "WAYNE JOHNSON",
        "expenditures": 120241,
        "contributions": 179848,
        "count": 74
  },
    {
        "name": "STEPHEN PAUL FRENCH",
        "expenditures": 179417,
        "contributions": 179565,
        "count": 146
  },
    {
        "name": "HENRY SANDERS",
        "expenditures": 105028,
        "contributions": 176115,
        "count": 73
  },
    {
        "name": "LARRY MEANS",
        "expenditures": 113384,
        "contributions": 175913,
        "count": 176
  },
    {
        "name": "CHRIS PRINGLE",
        "expenditures": 146850,
        "contributions": 174496,
        "count": 333
  },
    {
        "name": "VICTOR PHILLIPS POOLE JR.",
        "expenditures": 70250,
        "contributions": 173825,
        "count": 13
  },
    {
        "name": "BARRY RAMON SADLER SR.",
        "expenditures": 97496,
        "contributions": 169186,
        "count": 43
  },
    {
        "name": "CYNTHIA MCCARTY",
        "expenditures": 185743,
        "contributions": 168654,
        "count": 135
  },
    {
        "name": "LESLEY VANCE",
        "expenditures": 142957,
        "contributions": 166252,
        "count": 90
  },
    {
        "name": "CHARLES O. NEWTON",
        "expenditures": 102346,
        "contributions": 164773,
        "count": 86
  },
    {
        "name": "RICHARD GLO BAUGHN",
        "expenditures": 128678,
        "contributions": 164483,
        "count": 72
  },
    {
        "name": "DAVID LAWRENCE FAULKNER JR.",
        "expenditures": 130568,
        "contributions": 164381,
        "count": 364
  },
    {
        "name": "COREY P HARBISON",
        "expenditures": 56464,
        "contributions": 164196,
        "count": 64
  },
    {
        "name": "MARY SCOTT HUNTER",
        "expenditures": 182365,
        "contributions": 164105,
        "count": 177
  },
    {
        "name": "ARTHUR ORR",
        "expenditures": 15906,
        "contributions": 159308,
        "count": 101
  },
    {
        "name": "MELINDA MCCLENDON",
        "expenditures": 64965,
        "contributions": 153274,
        "count": 70
  },
    {
        "name": "SAMUEL A HARPER",
        "expenditures": 98080,
        "contributions": 152200,
        "count": 95
  },
    {
        "name": "JAMES C FIELDS JR.",
        "expenditures": 93438,
        "contributions": 145384,
        "count": 251
  },
    {
        "name": "JOHN ANDERSON CARTER SR.",
        "expenditures": 7631,
        "contributions": 144655,
        "count": 84
  },
    {
        "name": "THAD MCCLAMMY",
        "expenditures": 75600,
        "contributions": 142770,
        "count": 97
  },
    {
        "name": "DAN WILLIAMS",
        "expenditures": 93482,
        "contributions": 140526,
        "count": 83
  },
    {
        "name": "NATHANIEL DAVID LEDBETTER",
        "expenditures": 99406,
        "contributions": 138564,
        "count": 85
  },
    {
        "name": "STEVE DEAN",
        "expenditures": 123672,
        "contributions": 135472,
        "count": 31
  },
    {
        "name": "RANDY PRICE",
        "expenditures": 119319,
        "contributions": 134486,
        "count": 189
  },
    {
        "name": "GREG J REED",
        "expenditures": 49393,
        "contributions": 130354,
        "count": 107
  },
    {
        "name": "WALTER DON HEMBREE JR.",
        "expenditures": 121712,
        "contributions": 128602,
        "count": 65
  },
    {
        "name": "RODERICK HAMPTON SCOTT",
        "expenditures": 111399,
        "contributions": 127562,
        "count": 99
  },
    {
        "name": "MICHAEL MILLICAN",
        "expenditures": 40203,
        "contributions": 125254,
        "count": 97
  },
    {
        "name": "LARRY COLLINS STUTTS",
        "expenditures": 97117,
        "contributions": 125145,
        "count": 119
  },
    {
        "name": "AMIE BETH SHAVER",
        "expenditures": 91522,
        "contributions": 122290,
        "count": 81
  },
    {
        "name": "DOUGLAS CURTIS CLARK",
        "expenditures": 110751,
        "contributions": 121983,
        "count": 144
  },
    {
        "name": "KERRY RICH",
        "expenditures": 121318,
        "contributions": 120586,
        "count": 170
  },
    {
        "name": "TIM WADSWORTH",
        "expenditures": 52220,
        "contributions": 118942,
        "count": 79
  },
    {
        "name": "JOHN MCMILLAN",
        "expenditures": 52758,
        "contributions": 117419,
        "count": 158
  },
    {
        "name": "BILL HIGHTOWER",
        "expenditures": 27425,
        "contributions": 116467,
        "count": 123
  },
    {
        "name": "KYLE SOUTH",
        "expenditures": 71959,
        "contributions": 115246,
        "count": 123
  },
    {
        "name": "JOHN W WILLIAMS SR.",
        "expenditures": 84104,
        "contributions": 115117,
        "count": 135
  },
    {
        "name": "WILLIAM J AINSWORTH",
        "expenditures": 93899,
        "contributions": 113952,
        "count": 120
  },
    {
        "name": "JON CRAIG FORD",
        "expenditures": 33854,
        "contributions": 113948,
        "count": 79
  },
    {
        "name": "TIM SPRAYBERRY",
        "expenditures": 26797,
        "contributions": 110754,
        "count": 22
  },
    {
        "name": "JOSHUA PIPKIN",
        "expenditures": 130355,
        "contributions": 110387,
        "count": 185
  },
    {
        "name": "JAMES M MARTIN",
        "expenditures": 102129,
        "contributions": 110061,
        "count": 31
  },
    {
        "name": "DONALD MICHAEL RAINEY",
        "expenditures": 125200,
        "contributions": 108840,
        "count": 108
  },
    {
        "name": "BOBBY D SINGLETON",
        "expenditures": 76412,
        "contributions": 108769,
        "count": 42
  },
    {
        "name": "PERRYN CARROLL",
        "expenditures": 103474,
        "contributions": 108276,
        "count": 266
  },
    {
        "name": "JAY A. YORK",
        "expenditures": 118037,
        "contributions": 108142,
        "count": 301
  },
    {
        "name": "PATRICK JAMES BALLARD",
        "expenditures": 100810,
        "contributions": 107979,
        "count": 218
  },
    {
        "name": "STEPHEN (STEVE) WILCOX HURST",
        "expenditures": 97162,
        "contributions": 107323,
        "count": 70
  },
    {
        "name": "GAYLE HAYWOOD GEAR",
        "expenditures": 16428,
        "contributions": 103708,
        "count": 17
  },
    {
        "name": "MATTHEW DAVID FRIDY",
        "expenditures": 98478,
        "contributions": 103552,
        "count": 99
  },
    {
        "name": "GEORGE C BARRY",
        "expenditures": 99968,
        "contributions": 103511,
        "count": 12
  },
    {
        "name": "JOHN WESLEY ROGERS JR.",
        "expenditures": 90994,
        "contributions": 103300,
        "count": 51
  },
    {
        "name": "WILLIAM M \"BILLY\" BEASLEY",
        "expenditures": 17811,
        "contributions": 103250,
        "count": 45
  },
    {
        "name": "DAVID WILLIAM WHEELER",
        "expenditures": 102883,
        "contributions": 102652,
        "count": 117
  },
    {
        "name": "JAMES DARRELL TURNER",
        "expenditures": 80601,
        "contributions": 102628,
        "count": 704
  },
    {
        "name": "JOHN DANIEL GARRETT",
        "expenditures": 120251,
        "contributions": 101033,
        "count": 79
  },
    {
        "name": "CONNIE COONER ROWE",
        "expenditures": 39459,
        "contributions": 100614,
        "count": 181
  },
    {
        "name": "CAM WARD",
        "expenditures": 60175,
        "contributions": 99750,
        "count": 84
  },
    {
        "name": "RODGER MELL SMITHERMAN",
        "expenditures": 53504,
        "contributions": 96050,
        "count": 62
  },
    {
        "name": "HARRY SHIVER",
        "expenditures": 32856,
        "contributions": 95900,
        "count": 62
  },
    {
        "name": "PATRICIA ANN TODD",
        "expenditures": 75654,
        "contributions": 92100,
        "count": 219
  },
    {
        "name": "WILLIAM ISAAC WHORTON",
        "expenditures": 32973,
        "contributions": 91097,
        "count": 28
  },
    {
        "name": "RITCHIE AARON WHORTON",
        "expenditures": 67175,
        "contributions": 86501,
        "count": 105
  },
    {
        "name": "KEVIN MATTHEW GENTRY",
        "expenditures": 92217,
        "contributions": 86096,
        "count": 195
  },
    {
        "name": "MAX MICHAEL III",
        "expenditures": 85799,
        "contributions": 85810,
        "count": 200
  },
    {
        "name": "SAMUEL MARTIN COCHRAN",
        "expenditures": 54325,
        "contributions": 84311,
        "count": 284
  },
    {
        "name": "ARTIS J MCCAMPBELL",
        "expenditures": 79205,
        "contributions": 83892,
        "count": 89
  },
    {
        "name": "HARRY MCLEOD D'OLIVE JR.",
        "expenditures": 77472,
        "contributions": 83750,
        "count": 93
  },
    {
        "name": "JUANDALYNN D GIVAN",
        "expenditures": 77968,
        "contributions": 83700,
        "count": 73
  },
    {
        "name": "QUINTON T ROSS JR.",
        "expenditures": 44121,
        "contributions": 83250,
        "count": 36
  },
    {
        "name": "JONATHAN BERRYHILL",
        "expenditures": 82975,
        "contributions": 83039,
        "count": 91
  },
    {
        "name": "TERRY DUNN",
        "expenditures": 37672,
        "contributions": 80053,
        "count": 15
  },
    {
        "name": "DANIEL A. CROWSON",
        "expenditures": 75103,
        "contributions": 79455,
        "count": 195
  },
    {
        "name": "CHRIS SEIBERT",
        "expenditures": 94488,
        "contributions": 75617,
        "count": 80
  },
    {
        "name": "MAC MCCUTCHEON",
        "expenditures": 17676,
        "contributions": 75450,
        "count": 67
  },
    {
        "name": "CLAY DANIEL SCOFIELD",
        "expenditures": 19483,
        "contributions": 73800,
        "count": 58
  },
    {
        "name": "JAMES EDWARD BUSKEY",
        "expenditures": 40396,
        "contributions": 73528,
        "count": 85
  },
    {
        "name": "MIKE CURTIS",
        "expenditures": 38522,
        "contributions": 73348,
        "count": 35
  },
    {
        "name": "RICH ALLEN WINGO",
        "expenditures": 52266,
        "contributions": 73000,
        "count": 51
  },
    {
        "name": "MARK SLADE BLACKWELL",
        "expenditures": 223904,
        "contributions": 72966,
        "count": 82
  },
    {
        "name": "JOHNNY MACK MORROW",
        "expenditures": 24137,
        "contributions": 72650,
        "count": 78
  },
    {
        "name": "JAMES S ROBERTS JR.",
        "expenditures": 21257,
        "contributions": 72191,
        "count": 58
  },
    {
        "name": "STEVE CLOUSE",
        "expenditures": 69321,
        "contributions": 69680,
        "count": 171
  },
    {
        "name": "JAMES HORACE CLEMMONS JR.",
        "expenditures": 36003,
        "contributions": 69571,
        "count": 52
  },
    {
        "name": "MELVIN HASTING",
        "expenditures": 27888,
        "contributions": 68695,
        "count": 21
  },
    {
        "name": "ROBERT MCKAY",
        "expenditures": 20725,
        "contributions": 66726,
        "count": 69
  },
    {
        "name": "ROBERT REED INGRAM",
        "expenditures": 33038,
        "contributions": 66350,
        "count": 195
  },
    {
        "name": "BARBARA DRUMMOND",
        "expenditures": 50764,
        "contributions": 62477,
        "count": 146
  },
    {
        "name": "WILLIAM POOLE III",
        "expenditures": 24047,
        "contributions": 62385,
        "count": 63
  },
    {
        "name": "MARY KATHY PETERSON",
        "expenditures": 23884,
        "contributions": 61475,
        "count": 8
  },
    {
        "name": "ALAN C BOOTHE",
        "expenditures": 34317,
        "contributions": 60750,
        "count": 40
  },
    {
        "name": "DAVID BEDDINGFIELD",
        "expenditures": 31692,
        "contributions": 59928,
        "count": 90
  },
    {
        "name": "JIM ZEIGLER",
        "expenditures": 48325,
        "contributions": 59553,
        "count": 65
  },
    {
        "name": "RALPH ANTHONY HOWARD",
        "expenditures": 36607,
        "contributions": 59358,
        "count": 19
  },
    {
        "name": "KEN CLEO JOHNSON SR.",
        "expenditures": 8004,
        "contributions": 58312,
        "count": 44
  },
    {
        "name": "THOMAS BRYANT WHALEY",
        "expenditures": 35067,
        "contributions": 57855,
        "count": 64
  },
    {
        "name": "LINDA COLEMAN",
        "expenditures": 15525,
        "contributions": 56250,
        "count": 35
  },
    {
        "name": "MIKE HILL",
        "expenditures": 51184,
        "contributions": 55250,
        "count": 46
  },
    {
        "name": "TERRI COLLINS",
        "expenditures": 14982,
        "contributions": 55162,
        "count": 101
  },
    {
        "name": "ANDREW E BETTERTON",
        "expenditures": 13733,
        "contributions": 54301,
        "count": 33
  },
    {
        "name": "OLIVER LEON ROBINSON JR.",
        "expenditures": 65122,
        "contributions": 54100,
        "count": 51
  },
    {
        "name": "ROBERT HERMAN FINCHER",
        "expenditures": 26747,
        "contributions": 53696,
        "count": 123
  },
    {
        "name": "REX CHEATHAM",
        "expenditures": 9124,
        "contributions": 53395,
        "count": 62
  },
    {
        "name": "ELIZABETH \"BETH\" KELLUM",
        "expenditures": 10433,
        "contributions": 53100,
        "count": 4
  },
    {
        "name": "MERIKA COLEMAN",
        "expenditures": 26409,
        "contributions": 53085,
        "count": 60
  },
    {
        "name": "KENNETH MIKEAL PARSONS",
        "expenditures": 45132,
        "contributions": 52544,
        "count": 94
  },
    {
        "name": "RON ABERNATHY",
        "expenditures": 61434,
        "contributions": 52470,
        "count": 125
  },
    {
        "name": "WYNDALL A. IVEY",
        "expenditures": 16047,
        "contributions": 52344,
        "count": 143
  },
    {
        "name": "RONALD G JOHNSON",
        "expenditures": 19969,
        "contributions": 51670,
        "count": 58
  },
    {
        "name": "PATRICK DAVID PINKSTON",
        "expenditures": 52834,
        "contributions": 51513,
        "count": 121
  },
    {
        "name": "LAWRENCE MCADORY",
        "expenditures": 13738,
        "contributions": 50874,
        "count": 23
  },
    {
        "name": "DARIUS FOSTER",
        "expenditures": 35614,
        "contributions": 46671,
        "count": 145
  },
    {
        "name": "NAPOLEON BRACY JR.",
        "expenditures": 72416,
        "contributions": 46450,
        "count": 52
  },
    {
        "name": "PEGGY P MILLER LACHER",
        "expenditures": 46593,
        "contributions": 46310,
        "count": 162
  },
    {
        "name": "VIVIAN DAVIS FIGURES",
        "expenditures": 40235,
        "contributions": 46184,
        "count": 37
  },
    {
        "name": "TRIP PITTMAN",
        "expenditures": 19116,
        "contributions": 45445,
        "count": 54
  },
    {
        "name": "ADAM THOMPSON",
        "expenditures": 50222,
        "contributions": 45148,
        "count": 132
  },
    {
        "name": "BENJAMIN \"RUSTY\" N GLOVER III",
        "expenditures": 15831,
        "contributions": 44928,
        "count": 28
  },
    {
        "name": "MARK MCDONNELL TUGGLE",
        "expenditures": 26255,
        "contributions": 44813,
        "count": 68
  },
    {
        "name": "SHARON MAXWELL",
        "expenditures": 30106,
        "contributions": 44461,
        "count": 102
  },
    {
        "name": "JOHN AMARI",
        "expenditures": 52098,
        "contributions": 43913,
        "count": 133
  },
    {
        "name": "SHANTA CRAIG OWENS",
        "expenditures": 12672,
        "contributions": 43580,
        "count": 171
  },
    {
        "name": "CHARLIE L STATEN SR.",
        "expenditures": 28019,
        "contributions": 43000,
        "count": 11
  },
    {
        "name": "MIKE HOLMES",
        "expenditures": 26722,
        "contributions": 42772,
        "count": 60
  },
    {
        "name": "HOBBIE LEONARD SEALY",
        "expenditures": 35488,
        "contributions": 42526,
        "count": 34
  },
    {
        "name": "DAVID STANDRIDGE",
        "expenditures": 32497,
        "contributions": 42525,
        "count": 21
  },
    {
        "name": "PATRICIA MCGRIFF",
        "expenditures": 40694,
        "contributions": 42465,
        "count": 55
  },
    {
        "name": "CHRISTOPHER JOHN ENGLAND",
        "expenditures": 8964,
        "contributions": 42198,
        "count": 24
  },
    {
        "name": "BECKY NORDGREN",
        "expenditures": 21136,
        "contributions": 42059,
        "count": 35
  },
    {
        "name": "GINGER FLETCHER",
        "expenditures": 26354,
        "contributions": 42034,
        "count": 29
  },
    {
        "name": "FRANK WILLIAMSON",
        "expenditures": 38964,
        "contributions": 41080,
        "count": 71
  },
    {
        "name": "MATTHEW ALLEN MASSEY",
        "expenditures": 29113,
        "contributions": 40748,
        "count": 59
  },
    {
        "name": "MICHELLE M THOMASON",
        "expenditures": 25473,
        "contributions": 39889,
        "count": 153
  },
    {
        "name": "GEORGE TOOTIE BANDY",
        "expenditures": 19314,
        "contributions": 39470,
        "count": 19
  },
    {
        "name": "MICHAEL L JONES JR.",
        "expenditures": 22411,
        "contributions": 39440,
        "count": 81
  },
    {
        "name": "JIM MURPHREE",
        "expenditures": 34874,
        "contributions": 38526,
        "count": 45
  },
    {
        "name": "JACKIE MARK YARBROUGH",
        "expenditures": 43925,
        "contributions": 37715,
        "count": 21
  },
    {
        "name": "MICKY RAY HAMMON",
        "expenditures": 1309,
        "contributions": 37300,
        "count": 31
  },
    {
        "name": "MARTIN E WEINBERG",
        "expenditures": 30414,
        "contributions": 37217,
        "count": 143
  },
    {
        "name": "BAYLESS LYNN GREER",
        "expenditures": 5690,
        "contributions": 36850,
        "count": 33
  },
    {
        "name": "JOSEPH WHITCOMB SEDINGER",
        "expenditures": 32047,
        "contributions": 35864,
        "count": 134
  },
    {
        "name": "JOSEPH BRYAN D'ANGELO",
        "expenditures": 28733,
        "contributions": 35758,
        "count": 38
  },
    {
        "name": "RODGER DALE PETERSON",
        "expenditures": 20449,
        "contributions": 35074,
        "count": 6
  },
    {
        "name": "JOHN J LETSON",
        "expenditures": 3106,
        "contributions": 33633,
        "count": 2
  },
    {
        "name": "ANGELO DOC2565 MANCUSO",
        "expenditures": 28467,
        "contributions": 33616,
        "count": 9
  },
    {
        "name": "JAMES M. PATTERSON JR.",
        "expenditures": 33830,
        "contributions": 32888,
        "count": 69
  },
    {
        "name": "GEORGE \"CHUCK\" LEONARD PATTERSON JR.",
        "expenditures": 29582,
        "contributions": 32870,
        "count": 29
  },
    {
        "name": "JIM BARTON",
        "expenditures": 46012,
        "contributions": 32750,
        "count": 12
  },
    {
        "name": "BOBBY WAYNE JACKSON",
        "expenditures": 18701,
        "contributions": 32284,
        "count": 20
  },
    {
        "name": "RANDAL FORREST CAVNAR",
        "expenditures": 30399,
        "contributions": 32198,
        "count": 64
  },
    {
        "name": "JENNIFER SIGNE MARSDEN",
        "expenditures": 15845,
        "contributions": 32151,
        "count": 38
  },
    {
        "name": "RANDY VEST",
        "expenditures": 28928,
        "contributions": 32024,
        "count": 101
  },
    {
        "name": "BRENDA S. STEDHAM",
        "expenditures": 29102,
        "contributions": 31729,
        "count": 75
  },
    {
        "name": "JOHN ROBINSON",
        "expenditures": 20567,
        "contributions": 31700,
        "count": 16
  },
    {
        "name": "BERRY FORTE",
        "expenditures": 9459,
        "contributions": 31500,
        "count": 18
  },
    {
        "name": "JUSTIN BARKLEY",
        "expenditures": 23680,
        "contributions": 31240,
        "count": 75
  },
    {
        "name": "DONNIE CHESTEEN",
        "expenditures": 18350,
        "contributions": 30950,
        "count": 37
  },
    {
        "name": "JODY TRAUTWEIN",
        "expenditures": 26956,
        "contributions": 30913,
        "count": 110
  },
    {
        "name": "DAVID MONTGOMERY BLAIR",
        "expenditures": 27727,
        "contributions": 30732,
        "count": 91
  },
    {
        "name": "SUSAN ELAINE SMITH",
        "expenditures": 23166,
        "contributions": 30422,
        "count": 49
  },
    {
        "name": "CARL D SHERROD",
        "expenditures": 15231,
        "contributions": 30266,
        "count": 79
  },
    {
        "name": "C. TERRY JONES",
        "expenditures": 50889,
        "contributions": 29486,
        "count": 15
  },
    {
        "name": "DIMITRI POLIZOS",
        "expenditures": 17248,
        "contributions": 29292,
        "count": 32
  },
    {
        "name": "CYNTHIA A. BELL",
        "expenditures": 27004,
        "contributions": 29291,
        "count": 155
  },
    {
        "name": "BRUCE WHITLOCK",
        "expenditures": 23363,
        "contributions": 29194,
        "count": 7
  },
    {
        "name": "DICK L. BREWBAKER",
        "expenditures": 46428,
        "contributions": 28750,
        "count": 20
  },
    {
        "name": "BRIAN KEITH FOLEY",
        "expenditures": 9248,
        "contributions": 28635,
        "count": 9
  },
    {
        "name": "GARRY ROBERT MARCHMAN",
        "expenditures": 24090,
        "contributions": 28007,
        "count": 88
  },
    {
        "name": "JONATHAN O BARBEE",
        "expenditures": 16671,
        "contributions": 27994,
        "count": 79
  },
    {
        "name": "PRISCILLA P DUNN",
        "expenditures": 35679,
        "contributions": 27150,
        "count": 19
  },
    {
        "name": "RANDALL (RANDY) M DAVIS",
        "expenditures": 8394,
        "contributions": 26750,
        "count": 35
  },
    {
        "name": "RICHARD KEITH COATES",
        "expenditures": 22852,
        "contributions": 26179,
        "count": 77
  },
    {
        "name": "DYLAN VAN OLIVER",
        "expenditures": 6505,
        "contributions": 26116,
        "count": 2
  },
    {
        "name": "DANNY BROCK JOYNER",
        "expenditures": 12462,
        "contributions": 26001,
        "count": 19
  },
    {
        "name": "WILLIAM JOSHUA BURNS",
        "expenditures": 10609,
        "contributions": 25900,
        "count": 5
  },
    {
        "name": "JIM CARNS",
        "expenditures": 16207,
        "contributions": 25750,
        "count": 27
  },
    {
        "name": "MARY \"BETTY\" E PETERS",
        "expenditures": 16083,
        "contributions": 25569,
        "count": 47
  },
    {
        "name": "PEBBLIN WALKER WARREN",
        "expenditures": 7577,
        "contributions": 25500,
        "count": 15
  },
    {
        "name": "ALBERT DAVID JOHNSON",
        "expenditures": 21408,
        "contributions": 25299,
        "count": 41
  },
    {
        "name": "JAMES HOWARD SANDERFORD",
        "expenditures": 15581,
        "contributions": 24725,
        "count": 34
  },
    {
        "name": "RICK NEEDHAM",
        "expenditures": 31621,
        "contributions": 24662,
        "count": 77
  },
    {
        "name": "PAUL WESLEY LEE",
        "expenditures": 12180,
        "contributions": 24534,
        "count": 34
  },
    {
        "name": "MARY ANN MOORE",
        "expenditures": 47415,
        "contributions": 24136,
        "count": 29
  },
    {
        "name": "ARTHUR SHORES LEE",
        "expenditures": 24070,
        "contributions": 23595,
        "count": 44
  },
    {
        "name": "MARCEL BLACK",
        "expenditures": 20238,
        "contributions": 23300,
        "count": 28
  },
    {
        "name": "LOUISE UNITA ALEXANDER",
        "expenditures": 610,
        "contributions": 23000,
        "count": 5
  },
    {
        "name": "ANTHONY DANIELS JR.",
        "expenditures": 20541,
        "contributions": 22527,
        "count": 177
  },
    {
        "name": "JOHN WILLIAM COLE",
        "expenditures": 3895,
        "contributions": 22511,
        "count": 28
  },
    {
        "name": "WILLIAM DEXTER GRIMSLEY",
        "expenditures": 16763,
        "contributions": 22215,
        "count": 20
  },
    {
        "name": "MIKE BALL",
        "expenditures": 13885,
        "contributions": 21950,
        "count": 37
  },
    {
        "name": "HEATHER SELLERS",
        "expenditures": 45113,
        "contributions": 21831,
        "count": 97
  },
    {
        "name": "DONALD ROYCE MITCHELL",
        "expenditures": 21765,
        "contributions": 21769,
        "count": 56
  },
    {
        "name": "BRYAN EARL MORGAN",
        "expenditures": 15173,
        "contributions": 21726,
        "count": 27
  },
    {
        "name": "HUGH M DUDLEY JR.",
        "expenditures": 12582,
        "contributions": 21667,
        "count": 4
  },
    {
        "name": "MEREDITH PETERS",
        "expenditures": 18409,
        "contributions": 21472,
        "count": 65
  },
    {
        "name": "VICTOR GASTON",
        "expenditures": 10738,
        "contributions": 21450,
        "count": 21
  },
    {
        "name": "WALTON WARD HICKMAN",
        "expenditures": 3684,
        "contributions": 21393,
        "count": 14
  },
    {
        "name": "YOUNG J BOOZER III",
        "expenditures": 8394,
        "contributions": 21122,
        "count": 18
  },
    {
        "name": "CHARLES H. BOOHAKER",
        "expenditures": 14542,
        "contributions": 20929,
        "count": 35
  },
    {
        "name": "JIM HILL",
        "expenditures": 2331,
        "contributions": 20849,
        "count": 33
  },
    {
        "name": "THOMAS O. MOORE",
        "expenditures": 20623,
        "contributions": 20621,
        "count": 55
  },
    {
        "name": "RICHARD J. LINDSEY",
        "expenditures": 7791,
        "contributions": 20550,
        "count": 19
  },
    {
        "name": "DANIEL H BOMAN",
        "expenditures": 20154,
        "contributions": 20500,
        "count": 5
  },
    {
        "name": "HILDA J ETIENNE",
        "expenditures": 14988,
        "contributions": 20428,
        "count": 38
  },
    {
        "name": "CHERYL RINGUETTE CIAMARRA",
        "expenditures": 22199,
        "contributions": 20270,
        "count": 79
  },
    {
        "name": "BILLY ALFRED HODGES",
        "expenditures": 20939,
        "contributions": 20176,
        "count": 14
  },
    {
        "name": "JAMES WILLIAM BONNER",
        "expenditures": 6671,
        "contributions": 19999,
        "count": 1
  },
    {
        "name": "COLLINS PETTAWAY JR.",
        "expenditures": 12416,
        "contributions": 19864,
        "count": 22
  },
    {
        "name": "JULIA MARGARET WILCOX",
        "expenditures": 20881,
        "contributions": 19854,
        "count": 21
  },
    {
        "name": "ALEX BALKCUM",
        "expenditures": 13148,
        "contributions": 19816,
        "count": 9
  },
    {
        "name": "CHRISTOPHER SCOTT MCNEIL",
        "expenditures": 15616,
        "contributions": 19751,
        "count": 29
  },
    {
        "name": "ALAN WAYNE BAKER",
        "expenditures": 6550,
        "contributions": 19649,
        "count": 19
  },
    {
        "name": "HENRY ABDUL HASEEB",
        "expenditures": 19522,
        "contributions": 19527,
        "count": 54
  },
    {
        "name": "JAMES GILBERT BERRYMAN",
        "expenditures": 18627,
        "contributions": 19499,
        "count": 75
  },
    {
        "name": "GREGORY D WREN",
        "expenditures": 16702,
        "contributions": 19250,
        "count": 8
  },
    {
        "name": "EDWIN EUGENE PRICE",
        "expenditures": 19174,
        "contributions": 19174,
        "count": 23
  },
    {
        "name": "BEAU ROBERT MARLAND DOOLITTLE II",
        "expenditures": 11851,
        "contributions": 18999,
        "count": 38
  },
    {
        "name": "LOWELL ADAM HADDER",
        "expenditures": 13739,
        "contributions": 18500,
        "count": 7
  },
    {
        "name": "JIMMY COLLIER",
        "expenditures": 25405,
        "contributions": 18225,
        "count": 70
  },
    {
        "name": "RICHARD J COCHRAN",
        "expenditures": 11169,
        "contributions": 18082,
        "count": 19
  },
    {
        "name": "MICHAEL JOHNSON",
        "expenditures": 16715,
        "contributions": 17823,
        "count": 48
  },
    {
        "name": "KOVEN L. BROWN",
        "expenditures": 10590,
        "contributions": 17644,
        "count": 19
  },
    {
        "name": "BILL FULLER",
        "expenditures": 7393,
        "contributions": 16705,
        "count": 10
  },
    {
        "name": "LILLIE JONES-OSBORNE",
        "expenditures": 14147,
        "contributions": 16388,
        "count": 31
  },
    {
        "name": "MELODY WALKER",
        "expenditures": 14327,
        "contributions": 16295,
        "count": 47
  },
    {
        "name": "WILLIAM C. \"BILL\" THOMPSON",
        "expenditures": 36683,
        "contributions": 15714,
        "count": 28
  },
    {
        "name": "LUCIE MCLEMORE",
        "expenditures": 15795,
        "contributions": 15684,
        "count": 18
  },
    {
        "name": "DONALD RAY MURPHY",
        "expenditures": 14136,
        "contributions": 15660,
        "count": 14
  },
    {
        "name": "LAURA V HALL",
        "expenditures": 17296,
        "contributions": 15482,
        "count": 23
  },
    {
        "name": "DICKIE DRAKE",
        "expenditures": 8190,
        "contributions": 15250,
        "count": 17
  },
    {
        "name": "EVERETT W. WESS",
        "expenditures": 14661,
        "contributions": 15229,
        "count": 75
  },
    {
        "name": "LINDA W. H. HENDERSON",
        "expenditures": 11382,
        "contributions": 15180,
        "count": 156
  },
    {
        "name": "OTIS LEE PATTERSON",
        "expenditures": 10661,
        "contributions": 15070,
        "count": 76
  },
    {
        "name": "BUFORD CLIFF MANN",
        "expenditures": 16833,
        "contributions": 14745,
        "count": 84
  },
    {
        "name": "JOSEPH E FREEMAN JR.",
        "expenditures": 9298,
        "contributions": 14625,
        "count": 46
  },
    {
        "name": "LAWRENCE CONAWAY",
        "expenditures": 8165,
        "contributions": 14606,
        "count": 104
  },
    {
        "name": "WARREN GLEA SARRELL JR.",
        "expenditures": 12416,
        "contributions": 14509,
        "count": 16
  },
    {
        "name": "ELAINE BEECH",
        "expenditures": 11062,
        "contributions": 14350,
        "count": 15
  },
    {
        "name": "GWENDOLYN B KELLEY",
        "expenditures": 14062,
        "contributions": 14274,
        "count": 17
  },
    {
        "name": "STEPHEN A. MCMILLAN",
        "expenditures": 7313,
        "contributions": 14100,
        "count": 20
  },
    {
        "name": "GREGORY K BURDINE",
        "expenditures": 22685,
        "contributions": 14100,
        "count": 23
  },
    {
        "name": "JEFFREY SCOTT CHUNN",
        "expenditures": 13764,
        "contributions": 14048,
        "count": 15
  },
    {
        "name": "PHILLIP J PETTUS",
        "expenditures": 13081,
        "contributions": 14047,
        "count": 41
  },
    {
        "name": "JIM PERDUE",
        "expenditures": 23814,
        "contributions": 14008,
        "count": 30
  },
    {
        "name": "CHARLES FREDRICK JOLY",
        "expenditures": 6360,
        "contributions": 14004,
        "count": 37
  },
    {
        "name": "DAVID SESSIONS",
        "expenditures": 3900,
        "contributions": 13900,
        "count": 19
  },
    {
        "name": "JOHN F KNIGHT JR.",
        "expenditures": 13377,
        "contributions": 13885,
        "count": 18
  },
    {
        "name": "DENNIS W STEPHENS",
        "expenditures": 11779,
        "contributions": 13519,
        "count": 10
  },
    {
        "name": "JEFFREY REX MCLAUGHLIN",
        "expenditures": 13448,
        "contributions": 13448,
        "count": 22
  },
    {
        "name": "PHILLIP RALPH ANDREWS",
        "expenditures": 11467,
        "contributions": 13435,
        "count": 47
  },
    {
        "name": "TEDDY JOE FAUST SR.",
        "expenditures": 9193,
        "contributions": 13417,
        "count": 16
  },
    {
        "name": "RANDALL SHEDD",
        "expenditures": 10715,
        "contributions": 13350,
        "count": 19
  },
    {
        "name": "ADAM GLENN RITCH",
        "expenditures": 9917,
        "contributions": 13261,
        "count": 49
  },
    {
        "name": "GARY DOBBS HEAD SR.",
        "expenditures": 7558,
        "contributions": 13251,
        "count": 51
  },
    {
        "name": "ADLINE CECELIA CLARKE",
        "expenditures": 1792,
        "contributions": 13100,
        "count": 18
  },
    {
        "name": "ORLANDO RAY WHITEHEAD SR.",
        "expenditures": 12250,
        "contributions": 13021,
        "count": 34
  },
    {
        "name": "DAVID COLSTON",
        "expenditures": 18450,
        "contributions": 12600,
        "count": 13
  },
    {
        "name": "RANDY WOOD",
        "expenditures": 13261,
        "contributions": 12500,
        "count": 17
  },
    {
        "name": "CAROLYN WALLACE",
        "expenditures": 13157,
        "contributions": 12498,
        "count": 18
  },
    {
        "name": "WESLEY SCOTT MOBLEY",
        "expenditures": 14812,
        "contributions": 12318,
        "count": 27
  },
    {
        "name": "APRIL C WEAVER",
        "expenditures": 14828,
        "contributions": 12262,
        "count": 25
  },
    {
        "name": "CHARLES LEON ELLIS JR.",
        "expenditures": 9626,
        "contributions": 11942,
        "count": 43
  },
    {
        "name": "BOBBY GENE HUMPHRYES JR.",
        "expenditures": 11382,
        "contributions": 11596,
        "count": 10
  },
    {
        "name": "CHRISTOPHER LEE BYRD",
        "expenditures": 10445,
        "contributions": 11367,
        "count": 14
  },
    {
        "name": "BARBARA BIGSBY BOYD",
        "expenditures": 29660,
        "contributions": 11200,
        "count": 19
  },
    {
        "name": "S. PHILLIP BAHAKEL",
        "expenditures": 3504,
        "contributions": 11200,
        "count": 2
  },
    {
        "name": "REGINA HARRIS MCDONALD",
        "expenditures": 3650,
        "contributions": 11153,
        "count": 19
  },
    {
        "name": "SUZELLE MARIE JOSEY",
        "expenditures": 21687,
        "contributions": 11085,
        "count": 53
  },
    {
        "name": "JASON SPENCER BLACK",
        "expenditures": 8490,
        "contributions": 10872,
        "count": 27
  },
    {
        "name": "WILLIAM JEFFERY PEACOCK",
        "expenditures": 8376,
        "contributions": 10861,
        "count": 33
  },
    {
        "name": "MICHAEL ADAM HUTCHINS",
        "expenditures": 10812,
        "contributions": 10823,
        "count": 31
  },
    {
        "name": "ROBERT THEODORE RUSS BAILEY",
        "expenditures": 14386,
        "contributions": 10810,
        "count": 49
  },
    {
        "name": "STANLEY GENE HILL",
        "expenditures": 7018,
        "contributions": 10648,
        "count": 46
  },
    {
        "name": "TAMMY L. IRONS",
        "expenditures": 30017,
        "contributions": 10502,
        "count": 7
  },
    {
        "name": "DENNIS FRANKLIN MEEKS",
        "expenditures": 15960,
        "contributions": 10350,
        "count": 21
  },
    {
        "name": "ALLEN FARLEY",
        "expenditures": 7994,
        "contributions": 10150,
        "count": 14
  },
    {
        "name": "JIMMY BRYAN POOL",
        "expenditures": 19030,
        "contributions": 9995,
        "count": 41
  },
    {
        "name": "TIJUANNA ADETUNJI",
        "expenditures": 7606,
        "contributions": 9930,
        "count": 62
  },
    {
        "name": "STEVE SMALL JR.",
        "expenditures": 9134,
        "contributions": 9875,
        "count": 9
  },
    {
        "name": "DARREN L FLOTT",
        "expenditures": 8562,
        "contributions": 9765,
        "count": 16
  },
    {
        "name": "HOBBY WALKER",
        "expenditures": 8134,
        "contributions": 9730,
        "count": 10
  },
    {
        "name": "PHILLIP H BROWN",
        "expenditures": 5668,
        "contributions": 9677,
        "count": 20
  },
    {
        "name": "PAUL LEPAGE BECKMAN JR.",
        "expenditures": 11916,
        "contributions": 9650,
        "count": 11
  },
    {
        "name": "KELVIN J LAWRENCE",
        "expenditures": 8672,
        "contributions": 9500,
        "count": 12
  },
    {
        "name": "BOBBY LEWIS",
        "expenditures": 8866,
        "contributions": 9374,
        "count": 31
  },
    {
        "name": "TIMOTHY DAVID ROPER",
        "expenditures": 6399,
        "contributions": 9295,
        "count": 8
  },
    {
        "name": "DARRIO MELTON",
        "expenditures": 9350,
        "contributions": 9270,
        "count": 18
  },
    {
        "name": "SHERI WOOD CARVER",
        "expenditures": 8895,
        "contributions": 9258,
        "count": 28
  },
    {
        "name": "JOEL BLANKENSHIP",
        "expenditures": 8679,
        "contributions": 9080,
        "count": 33
  },
    {
        "name": "WAYNE E BIGGS",
        "expenditures": 7111,
        "contributions": 9026,
        "count": 25
  },
    {
        "name": "SONYA PATTERSON",
        "expenditures": 8226,
        "contributions": 9013,
        "count": 48
  },
    {
        "name": "WILLIAM A BARNES",
        "expenditures": 4785,
        "contributions": 8572,
        "count": 9
  },
    {
        "name": "MARY B WINDOM",
        "expenditures": 156202,
        "contributions": 8531,
        "count": 5
  },
    {
        "name": "PATRICK SELLERS",
        "expenditures": 7662,
        "contributions": 8505,
        "count": 13
  },
    {
        "name": "DEBORAH HILL BIGGERS",
        "expenditures": 8255,
        "contributions": 8409,
        "count": 31
  },
    {
        "name": "ANTHONY ALANN JOHNSON",
        "expenditures": 7900,
        "contributions": 8200,
        "count": 15
  },
    {
        "name": "PAMELA BLACKMORE-JENKINS",
        "expenditures": 7490,
        "contributions": 8190,
        "count": 9
  },
    {
        "name": "LESA GRIFFITH KEITH",
        "expenditures": 8163,
        "contributions": 8170,
        "count": 63
  },
    {
        "name": "ALAN BRYANT GRABEN",
        "expenditures": 7679,
        "contributions": 8083,
        "count": 21
  },
    {
        "name": "BENJAMIN ALLEN TREADAWAY",
        "expenditures": 5411,
        "contributions": 8000,
        "count": 12
  },
    {
        "name": "JOHN ANTHONY SAVAGE",
        "expenditures": 6268,
        "contributions": 7972,
        "count": 10
  },
    {
        "name": "JOEL LEE WILLIAMS",
        "expenditures": 4717,
        "contributions": 7926,
        "count": 25
  },
    {
        "name": "JIM GREEN SR.",
        "expenditures": 6334,
        "contributions": 7728,
        "count": 11
  },
    {
        "name": "SUZANNE CHILDERS",
        "expenditures": 6571,
        "contributions": 7643,
        "count": 25
  },
    {
        "name": "PHILLIP ROSS MCGLAUGHN",
        "expenditures": 7608,
        "contributions": 7595,
        "count": 36
  },
    {
        "name": "MARTHA BARBER HUMPHREY",
        "expenditures": 7113,
        "contributions": 7557,
        "count": 12
  },
    {
        "name": "TERRY DUANE MCGEE",
        "expenditures": 6206,
        "contributions": 7526,
        "count": 26
  },
    {
        "name": "TANYA TOLBERT ROBERTS",
        "expenditures": 7509,
        "contributions": 7521,
        "count": 12
  },
    {
        "name": "STACY LEE GEORGE",
        "expenditures": 4052,
        "contributions": 7352,
        "count": 32
  },
    {
        "name": "DAVID BERT YOUNG JR.",
        "expenditures": 5680,
        "contributions": 7350,
        "count": 15
  },
    {
        "name": "CHARLES RANDAL BROCK",
        "expenditures": 9393,
        "contributions": 7300,
        "count": 14
  },
    {
        "name": "JOE E BASENBERG",
        "expenditures": 0,
        "contributions": 7223,
        "count": 26
  },
    {
        "name": "JOHN BAHAKEL",
        "expenditures": 1931,
        "contributions": 7040,
        "count": 15
  },
    {
        "name": "THOMAS E ACTION JACKSON",
        "expenditures": 15970,
        "contributions": 7000,
        "count": 8
  },
    {
        "name": "DONALD EDWARD BARNWELL",
        "expenditures": 7344,
        "contributions": 6850,
        "count": 7
  },
    {
        "name": "WILSON EDWARD ROWELL",
        "expenditures": 4716,
        "contributions": 6812,
        "count": 29
  },
    {
        "name": "MIRANDA SCHRUBBE",
        "expenditures": 5990,
        "contributions": 6754,
        "count": 22
  },
    {
        "name": "KENNETH LYNN BAILEY",
        "expenditures": 6218,
        "contributions": 6533,
        "count": 25
  },
    {
        "name": "JAMES MACDONALD RUSSELL JR.",
        "expenditures": 5254,
        "contributions": 6530,
        "count": 37
  },
    {
        "name": "MIRANDA KARRINE JOSEPH",
        "expenditures": 5063,
        "contributions": 6483,
        "count": 56
  },
    {
        "name": "JANE SMITH",
        "expenditures": 3260,
        "contributions": 6450,
        "count": 30
  },
    {
        "name": "WILLIE A CASEY",
        "expenditures": 945,
        "contributions": 6425,
        "count": 8
  },
    {
        "name": "JAMES \"JAMEY\" HOWARD CLEMENTS JR.",
        "expenditures": 6927,
        "contributions": 6349,
        "count": 13
  },
    {
        "name": "VJ VIVIAN FORD",
        "expenditures": 1715,
        "contributions": 6255,
        "count": 47
  },
    {
        "name": "JEREMY HEATH JACKSON",
        "expenditures": 3403,
        "contributions": 6200,
        "count": 11
  },
    {
        "name": "SHIRLEY A SCOTT-HARRIS",
        "expenditures": 2357,
        "contributions": 6165,
        "count": 42
  },
    {
        "name": "JAMES (RON) WILSON III",
        "expenditures": 21505,
        "contributions": 6110,
        "count": 5
  },
    {
        "name": "WILLIAM DAVIS LAWLEY JR.",
        "expenditures": 4092,
        "contributions": 6000,
        "count": 2
  },
    {
        "name": "WESLEY JARON HODGES",
        "expenditures": 5809,
        "contributions": 5933,
        "count": 40
  },
    {
        "name": "THEODORE A COPLAND II",
        "expenditures": 3700,
        "contributions": 5918,
        "count": 13
  },
    {
        "name": "GINGER POYNTER",
        "expenditures": 1099,
        "contributions": 5773,
        "count": 20
  },
    {
        "name": "LATUNJA ADAMS CASTER",
        "expenditures": 3783,
        "contributions": 5753,
        "count": 22
  },
    {
        "name": "PHIL WILLIAMS",
        "expenditures": 4041,
        "contributions": 5650,
        "count": 8
  },
    {
        "name": "RON STEVEN CRUMPTON",
        "expenditures": 4743,
        "contributions": 5623,
        "count": 37
  },
    {
        "name": "DAVID ALAN COPELAND",
        "expenditures": 5569,
        "contributions": 5571,
        "count": 15
  },
    {
        "name": "GERALD C WALLACE",
        "expenditures": 5992,
        "contributions": 5549,
        "count": 20
  },
    {
        "name": "ROY D. JACKSON",
        "expenditures": 7793,
        "contributions": 5350,
        "count": 19
  },
    {
        "name": "JERRY ALAN MCGILVRAY",
        "expenditures": 3657,
        "contributions": 5237,
        "count": 20
  },
    {
        "name": "RAY BRYAN",
        "expenditures": 5586,
        "contributions": 5200,
        "count": 10
  },
    {
        "name": "ROBERT W. GREEN",
        "expenditures": 5048,
        "contributions": 5150,
        "count": 38
  },
    {
        "name": "FRANKLIN W CHANDLER JR.",
        "expenditures": 5093,
        "contributions": 5116,
        "count": 6
  },
    {
        "name": "TILLMAN PUGH",
        "expenditures": 2617,
        "contributions": 5024,
        "count": 8
  },
    {
        "name": "GREG SHAW",
        "expenditures": 11973,
        "contributions": 5000,
        "count": 2
  },
    {
        "name": "THOMAS GENE FARMER",
        "expenditures": 4325,
        "contributions": 5000,
        "count": 1
  },
    {
        "name": "FRED JOLY",
        "expenditures": 7198,
        "contributions": 5000,
        "count": 1
  },
    {
        "name": "J.R. GAINES",
        "expenditures": 17053,
        "contributions": 4950,
        "count": 29
  },
    {
        "name": "JAMES THOMAS HANES JR.",
        "expenditures": 2947,
        "contributions": 4929,
        "count": 15
  },
    {
        "name": "WILLIAM MCCALL HARRIS JR.",
        "expenditures": 3976,
        "contributions": 4878,
        "count": 10
  },
    {
        "name": "STERLING JOSH STATOM SR.",
        "expenditures": 4745,
        "contributions": 4746,
        "count": 11
  },
    {
        "name": "ELLENE SCHELL BROWN",
        "expenditures": 5241,
        "contributions": 4550,
        "count": 8
  },
    {
        "name": "GUY KELLY",
        "expenditures": 4496,
        "contributions": 4496,
        "count": 9
  },
    {
        "name": "ANTHONY AVON CLARKBANKS",
        "expenditures": 4386,
        "contributions": 4406,
        "count": 73
  },
    {
        "name": "JARED FREEMAN",
        "expenditures": 7456,
        "contributions": 4306,
        "count": 12
  },
    {
        "name": "MARY ANN DEES",
        "expenditures": 4295,
        "contributions": 4301,
        "count": 17
  },
    {
        "name": "JIMMIE L BENISON SR.",
        "expenditures": 4175,
        "contributions": 4178,
        "count": 7
  },
    {
        "name": "APRIL LANCASTER LOGAN-RUSSELL",
        "expenditures": 3183,
        "contributions": 4132,
        "count": 5
  },
    {
        "name": "HANDLEY JEFF HARDY",
        "expenditures": 3912,
        "contributions": 4075,
        "count": 10
  },
    {
        "name": "HENRY ALLRED",
        "expenditures": 7456,
        "contributions": 4000,
        "count": 6
  },
    {
        "name": "THOMAS SLOAN",
        "expenditures": 3682,
        "contributions": 3915,
        "count": 4
  },
    {
        "name": "WILLIAM SCOTT DONALDSON",
        "expenditures": 12141,
        "contributions": 3850,
        "count": 3
  },
    {
        "name": "ROBERT KEVIN BASS",
        "expenditures": 3259,
        "contributions": 3842,
        "count": 6
  },
    {
        "name": "JIMMY LEON BELL",
        "expenditures": 4360,
        "contributions": 3821,
        "count": 7
  },
    {
        "name": "JOHN E. AMARI",
        "expenditures": 2090,
        "contributions": 3800,
        "count": 6
  },
    {
        "name": "BRYAN MCDANIEL TAYLOR",
        "expenditures": 3983,
        "contributions": 3750,
        "count": 4
  },
    {
        "name": "WILLIAM HENRY STRICKLEND III",
        "expenditures": 2020,
        "contributions": 3750,
        "count": 10
  },
    {
        "name": "JOE COTTLE",
        "expenditures": 3704,
        "contributions": 3704,
        "count": 2
  },
    {
        "name": "DENISE HUMBURG",
        "expenditures": 3936,
        "contributions": 3700,
        "count": 3
  },
    {
        "name": "MORRIS DAVID CUMMINGS JR.",
        "expenditures": 2249,
        "contributions": 3652,
        "count": 8
  },
    {
        "name": "JIM GRIGGS",
        "expenditures": 3484,
        "contributions": 3486,
        "count": 5
  },
    {
        "name": "JOHN RALPH SAUNDERS",
        "expenditures": 3395,
        "contributions": 3450,
        "count": 7
  },
    {
        "name": "JAMES BERRY SHANNON JR.",
        "expenditures": 3194,
        "contributions": 3350,
        "count": 6
  },
    {
        "name": "MICHAEL JASON GLADDEN",
        "expenditures": 23096,
        "contributions": 3345,
        "count": 11
  },
    {
        "name": "LATEEFAH MUHAMMAD",
        "expenditures": 3467,
        "contributions": 3318,
        "count": 38
  },
    {
        "name": "SCOTT BEASON",
        "expenditures": 2441,
        "contributions": 3250,
        "count": 4
  },
    {
        "name": "SHADRACK DWIGHT MCGILL",
        "expenditures": 128,
        "contributions": 3125,
        "count": 1
  },
    {
        "name": "SHADRACK MCGILL",
        "expenditures": 2960,
        "contributions": 3038,
        "count": 9
  },
    {
        "name": "HENRY A WHITE",
        "expenditures": 5569,
        "contributions": 2900,
        "count": 3
  },
    {
        "name": "MONICA ANGELISA SWIGER",
        "expenditures": 1823,
        "contributions": 2806,
        "count": 3
  },
    {
        "name": "RONNIE REED",
        "expenditures": 2743,
        "contributions": 2743,
        "count": 5
  },
    {
        "name": "KATY S CAMPBELL",
        "expenditures": 2360,
        "contributions": 2704,
        "count": 29
  },
    {
        "name": "JOHN HENRY ENGLAND JR.",
        "expenditures": 3350,
        "contributions": 2598,
        "count": 2
  },
    {
        "name": "CHAD A LAQUA",
        "expenditures": 2546,
        "contributions": 2546,
        "count": 1
  },
    {
        "name": "CHARLES BERNARD LANGHAM",
        "expenditures": 2397,
        "contributions": 2500,
        "count": 1
  },
    {
        "name": "STEPHANIE E. ENGLE",
        "expenditures": 1498,
        "contributions": 2500,
        "count": 1
  },
    {
        "name": "JOHN HARDY",
        "expenditures": 2006,
        "contributions": 2429,
        "count": 6
  },
    {
        "name": "STEVEN LAMAR WHITMIRE II",
        "expenditures": 2378,
        "contributions": 2428,
        "count": 2
  },
    {
        "name": "JENIFER C HOLT",
        "expenditures": 2417,
        "contributions": 2417,
        "count": 2
  },
    {
        "name": "M. RYAN RUMSEY",
        "expenditures": 2398,
        "contributions": 2398,
        "count": 1
  },
    {
        "name": "CHUCK MALONE",
        "expenditures": 2398,
        "contributions": 2398,
        "count": 1
  },
    {
        "name": "BRENT M CRAIG",
        "expenditures": 2389,
        "contributions": 2388,
        "count": 2
  },
    {
        "name": "TAMMY JACKSON MONTGOMERY",
        "expenditures": 2378,
        "contributions": 2380,
        "count": 1
  },
    {
        "name": "DON WORD",
        "expenditures": 2378,
        "contributions": 2378,
        "count": 1
  },
    {
        "name": "JONATHAN A BROWN",
        "expenditures": 2378,
        "contributions": 2378,
        "count": 1
  },
    {
        "name": "MITCHELL JOHN HOWIE",
        "expenditures": 1366,
        "contributions": 2366,
        "count": 3
  },
    {
        "name": "FRANK BERTARELLI",
        "expenditures": 4590,
        "contributions": 2300,
        "count": 3
  },
    {
        "name": "LAMAR HEATH JONES",
        "expenditures": 1531,
        "contributions": 2285,
        "count": 13
  },
    {
        "name": "CHARLOTTE BORDEN MEADOWS",
        "expenditures": 24227,
        "contributions": 2250,
        "count": 6
  },
    {
        "name": "AMANDA G SCOTT",
        "expenditures": 1643,
        "contributions": 2250,
        "count": 11
  },
    {
        "name": "JAMES FLETCHER HUGHEY III",
        "expenditures": 371,
        "contributions": 2000,
        "count": 1
  },
    {
        "name": "WILLIAM STANLEY GARNER JR.",
        "expenditures": 2378,
        "contributions": 2000,
        "count": 1
  },
    {
        "name": "TRACY LEON HAWSEY",
        "expenditures": 1463,
        "contributions": 1850,
        "count": 4
  },
    {
        "name": "ROBERT LAKE MINOR",
        "expenditures": 2378,
        "contributions": 1800,
        "count": 1
  },
    {
        "name": "TONTA DRAPER",
        "expenditures": 212,
        "contributions": 1800,
        "count": 2
  },
    {
        "name": "BRIAN DOUGLAS BROOKS",
        "expenditures": 0,
        "contributions": 1755,
        "count": 5
  },
    {
        "name": "RALPH CHARLES CARMICHAEL SR.",
        "expenditures": 1735,
        "contributions": 1736,
        "count": 2
  },
    {
        "name": "BRYAN BENNETT",
        "expenditures": 1293,
        "contributions": 1687,
        "count": 5
  },
    {
        "name": "ANGELA LAREESE FEARS",
        "expenditures": 379,
        "contributions": 1595,
        "count": 4
  },
    {
        "name": "JOHN D. JAMES",
        "expenditures": 1393,
        "contributions": 1593,
        "count": 2
  },
    {
        "name": "JAMES ANTHONY ZACHERO JR.",
        "expenditures": 428,
        "contributions": 1592,
        "count": 5
  },
    {
        "name": "JOHN WAYNE YOUNG",
        "expenditures": 253,
        "contributions": 1500,
        "count": 3
  },
    {
        "name": "JOHN MICHAEL MASTIN",
        "expenditures": 3027,
        "contributions": 1325,
        "count": 10
  },
    {
        "name": "MICHAEL LYNN WILLIAMS",
        "expenditures": 1244,
        "contributions": 1244,
        "count": 3
  },
    {
        "name": "STEPHEN PATRICK CARR II",
        "expenditures": 868,
        "contributions": 1220,
        "count": 18
  },
    {
        "name": "DOUGLAS L NEIGHBORS JR.",
        "expenditures": 1099,
        "contributions": 1154,
        "count": 8
  },
    {
        "name": "SUSAN B HIGHTOWER",
        "expenditures": 6507,
        "contributions": 1025,
        "count": 3
  },
    {
        "name": "JOHN ADAMS",
        "expenditures": 744,
        "contributions": 1000,
        "count": 1
  },
    {
        "name": "CHAD AUSTIN FINCHER",
        "expenditures": 3263,
        "contributions": 1000,
        "count": 1
  },
    {
        "name": "JOHNNY HARDWICK",
        "expenditures": 6039,
        "contributions": 1000,
        "count": 2
  },
    {
        "name": "BARRY SCOTT WILLINGHAM",
        "expenditures": 860,
        "contributions": 910,
        "count": 3
  },
    {
        "name": "TRAVIS DEREL COLQUETT",
        "expenditures": 662,
        "contributions": 725,
        "count": 3
  },
    {
        "name": "CARMEN BOSCH",
        "expenditures": 2587,
        "contributions": 723,
        "count": 9
  },
    {
        "name": "ALISON AUSTIN",
        "expenditures": 4223,
        "contributions": 700,
        "count": 2
  },
    {
        "name": "HEATH JONES",
        "expenditures": 632,
        "contributions": 538,
        "count": 6
  },
    {
        "name": "CURTIS HARVEY",
        "expenditures": 1356,
        "contributions": 500,
        "count": 1
  },
    {
        "name": "JAY KENNETH LOVE",
        "expenditures": 5176,
        "contributions": 408,
        "count": 1
  },
    {
        "name": "EUGENE REESE",
        "expenditures": 6152,
        "contributions": 221,
        "count": 3
  },
    {
        "name": "JESHUA D SCREWS",
        "expenditures": 219,
        "contributions": 219,
        "count": 4
  },
    {
        "name": "STEPHEN SEXTON",
        "expenditures": 34123,
        "contributions": 200,
        "count": 2
  },
    {
        "name": "LEIGH LACHINE",
        "expenditures": 0,
        "contributions": 176,
        "count": 3
  },
    {
        "name": "N",
        "expenditures": 0,
        "contributions": 100,
        "count": 1
  },
    {
        "name": "MITCHELL SCOTT FLOYD",
        "expenditures": 369,
        "contributions": 75,
        "count": 1
  },
    {
        "name": "HOWARD HAWK",
        "expenditures": 25483,
        "contributions": 58,
        "count": 3
  },
    {
        "name": "GREGORY M WILLIAMS",
        "expenditures": 2921,
        "contributions": 25,
        "count": 1
  },
    {
        "name": "OLIVER WESLEY LONG",
        "expenditures": 2099,
        "contributions": 3,
        "count": 1
  },
    {
        "name": "ROBERT L. BROUSSARD",
        "expenditures": 2504,
        "contributions": 2,
        "count": 1
  },
    {
        "name": "MARC KEAHEY",
        "expenditures": 5759,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "JOE NEAL HOWELL",
        "expenditures": 1357,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "JOSEPH LOUIS BOOHAKER",
        "expenditures": 1044,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "BRAD MENDHEIM",
        "expenditures": 2397,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "WILLIAM A. SHASHY",
        "expenditures": 6703,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "JAMIE ISON",
        "expenditures": 12789,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "LILES CLIFTON BURKE",
        "expenditures": 2966,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "BRADLEY R. BYRNE",
        "expenditures": 2375,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "J LANGFORD FLOYD",
        "expenditures": 2598,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "DALE W. STRONG",
        "expenditures": 20625,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "JACQUELYN \"LYN\" STUART",
        "expenditures": 4076,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "JAMES GLENN GOGGANS",
        "expenditures": 2378,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "TERRY WAYNE HENDRIX",
        "expenditures": 1798,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "JOSEPH MITCHELL",
        "expenditures": 2332,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "TOMMY ELIAS BRYAN",
        "expenditures": 12490,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "JOHN B. BUSH",
        "expenditures": 725,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "JAMES F ROBINSON JR.",
        "expenditures": 5283,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "SCHUYLER H. RICHARDSON III",
        "expenditures": 2928,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "CHRISTOPHER MICHAEL MCINTYRE",
        "expenditures": 59,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "RANDY THOMAS HESTER",
        "expenditures": 2369,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "ARTHUR L CRAWFOD SR.",
        "expenditures": 72,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "PAUL JOHN DEMARCO",
        "expenditures": 500,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "JEFFREY T BROCK",
        "expenditures": 1014,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "STEVEN D. KING",
        "expenditures": 405,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "MICHAEL G \"MIKE\" GRAFFEO",
        "expenditures": 2258,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "SCOTT PARKER TAYLOR",
        "expenditures": 58,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "ALAN MANN",
        "expenditures": 1668,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "KAREN KIMBRELL HALL",
        "expenditures": 41,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "BRAXTON PAUL SHERLING",
        "expenditures": 300,
        "contributions": 0,
        "count": 0
  },
    {
        "name": "TIMOTHY ALTON EVANS",
        "expenditures": 5,
        "contributions": 0,
        "count": 0
  }
]