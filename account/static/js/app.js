(function(){
var app= angular.module('account', []);
app.controller('accountcontroller', ['$scope', function($scope) {
    $scope.input = "entrez le nom du processus";
    $scope.name = 'voici le pid';

    $scope.getpid = function(name) {
    $scope.name = "123456789";
    };
}]);
})();

