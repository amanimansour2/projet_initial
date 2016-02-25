(function(){
var app= angular.module('account', []);
app.controller('accountcontroller', ['$scope','$http', function($scope,$http) {
    $scope.input = "entrez le nom du processus";
    $scope.name = 'voici le pid';

    $scope.getpid = function() {
     
        $http({
       method : "GET",
       url : "/account/test/",
       params:{"parameter" : "valeur"},
       }).then(function (response) {
         $scope.name = response.data.username;
           console.log('Success', "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh");
    // For JSON responses, resp.data contains the result
  }, function(err) {
    console.error('ERR', "ccccccccccccccccccccccccccccccccccccccccccccc");
    // err.status will contain the status code
    });}
}]);
})();

