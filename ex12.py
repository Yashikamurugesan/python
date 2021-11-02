from photocalendar import PhotoCalendar
calendar = PhotoCalendar( # not all arguments are mandatory
	outputBase                = "/some/output/base",
	year                      = 2019,
	firstWeekDay              = "Tu", # Tuesday as the first week day? Well, why not...
	imagesDirectory           = "/some/directory/with/images/for/each/week",
	imageDescriptionsFile     = "/some/file/with/image/descriptions/for/each/week",
	backgroundImagesDirectory = "/some/directory/with/backround/images/for/each/week",
	title                     = "Some calendar title",
	titlePageImage            = "/some/image/for/title/page",
	titlePageBackground       = "/some/background/image/for/titlepage",
	lastPageBackground        = "/some/background/image/for/last/page",
	nameDaysFile              = "/some/file/with/name-days",
	religiousHolidaysFile     = "/some/file/with/religious/holidays",
	publicHolidaysFile        = "/some/file/with/public/holidays",
	notesFile                 = "/some/file/with/notes/like/birthdays/etc",
	weekDayNamesFile          = "/some/file/with/custom/weekday/names",
	abbrWeekDayNamesFile      = "/some/file/with/custom/abbreviated/weekday/names",
	monthNamesFile            = "/some/file/with/custom/month/names",
	abbrMonthNamesFile        = "/some/file/with/custom/abbreviated/month/names",
	template                  = "delphinus",
)
calendar.toHTML()
