(function(){
var app= angular.module('account', []);
app.controller('accountcontroller', ['$scope','$http', function($scope,$http) {
    $scope.input = "entrez le nom du processus";
    $scope.name = 'voici le pid';

    $scope.getpid = function() {
     
        $http({
       method : "GET",
       url : "/account/test/",
       params:{"parameter" : "valeur_amani"},
       }).then(function (response) {
         $scope.name = response.data.username;
     });}
}]);
})();

