// Initialize all input of date type.
const calendars = bulmaCalendar.attach('[type="date"]')

// Loop on each calendar initialized
calendars.forEach(calendar => {
	// Add listener to select event
	calendar.on('select', date => {
		console.log(date)
	})
})
