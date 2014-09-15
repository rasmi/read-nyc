angular.module('readnyc', ['ui.bootstrap', 'ui.utils'])
.controller('signupCtrl', function($scope) {
	$scope.dayOptions = [
		{"value": "3", "label": "Any day of the week."},
		{"value": "1", "label": "Just weekends."},
		{"value": "2", "label": "Just weekdays."}
	]
	$scope.user = {}
	/*
	Upon entering zipcode, return nearest libraries. Ask user to pick their favorites. (no need to rank them). Show a map?

	On submit, send user data, validate (see if they already exist, get first/last names), store data, return appropriate response (including name and notification if user already exists).
	*/
	$scope.submit = function() {
		$scope.submitted = true;
	}

	$scope.$watch('user.zipcode', function(newValue, oldValue) {
		if (newValue) console.log(newValue);
		// Make a call to API, get nearest libraries.
	})
});