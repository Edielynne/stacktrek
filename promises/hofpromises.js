const countries = [
    { name: 'Afghanistan', population: 27657145 },
    { name: 'Åland Islands', population: 28875 },
    { name: 'Albania', population: 2886026 },
    { name: 'Algeria', population: 40400000 },
    { name: 'American Samoa', population: 57100 },
    { name: 'Andorra', population: 78014 },
    { name: 'Angola', population: 25868000 },
    { name: 'Anguilla', population: 13452 },
    { name: 'Antarctica', population: 1000 },
    { name: 'Antigua and Barbuda', population: 86295 },
    { name: 'Argentina', population: 43590400 },
    { name: 'Armenia', population: 2994400 },
    { name: 'Aruba', population: 107394 },
    { name: 'Australia', population: 24117360 },
    { name: 'Austria', population: 8725931 },
    { name: 'Azerbaijan', population: 9730500 },
    { name: 'Bahamas', population: 378040 },
    { name: 'Bahrain', population: 1404900 },
    { name: 'Bangladesh', population: 161006790 },
    { name: 'Barbados', population: 285000 },
    { name: 'Belarus', population: 9498700 },
    { name: 'Belgium', population: 11319511 },
    { name: 'Belize', population: 370300 },
    { name: 'Benin', population: 10653654 },
    { name: 'Bermuda', population: 61954 },
    { name: 'Bhutan', population: 775620 },
    { name: 'Bolivia (Plurinational State of)', population: 10985059 },
    { name: 'Bonaire, Sint Eustatius and Saba', population: 17408 },
    { name: 'Bosnia and Herzegovina', population: 3531159 },
    { name: 'Botswana', population: 2141206 },
    { name: 'Bouvet Island', population: 0 },
    { name: 'Brazil', population: 206135893 },
    { name: 'British Indian Ocean Territory', population: 3000 },
    { name: 'United States Minor Outlying Islands', population: 300 },
    { name: 'Virgin Islands (British)', population: 28514 },
    { name: 'Virgin Islands (U.S.)', population: 114743 },
    { name: 'Brunei Darussalam', population: 411900 },
    { name: 'Bulgaria', population: 7153784 },
    { name: 'Burkina Faso', population: 19034397 },
    { name: 'Burundi', population: 10114505 },
    { name: 'Cambodia', population: 15626444 },
    { name: 'Cameroon', population: 22709892 },
    { name: 'Canada', population: 36155487 },
    { name: 'Cabo Verde', population: 531239 },
    { name: 'Cayman Islands', population: 58238 },
    { name: 'Central African Republic', population: 4998000 },
    { name: 'Chad', population: 14497000 },
    { name: 'Chile', population: 18191900 },
    { name: 'China', population: 1377422166 },
    { name: 'Christmas Island', population: 2072 }
  ]
const userdata = [
    { fullName: 'connie_gulgowski', age: 26, salary: 37613 },
    { fullName: 'alana_beatty', age: 47, salary: 12427 },
    { fullName: 'marlon_hagenes', age: 55, salary: 47476 },
    { fullName: 'gregorio_bechtelar', age: 49, salary: 28977 },
    { fullName: 'greyson_wolf', age: 23, salary: 5971 },
    { fullName: 'elinor_bergnaum', age: 56, salary: 12683 },
    { fullName: 'kaitlin_wuckert', age: 38, salary: 14170 },
    { fullName: 'zachary_casper', age: 32, salary: 47909 },
    { fullName: 'serena_schuppe', age: 46, salary: 15311 },
    { fullName: 'emmitt_towne', age: 50, salary: 39088 },
    { fullName: 'jamal_schowalter', age: 17, salary: 47427 },
    { fullName: 'adrienne_carter', age: 55, salary: 13149 },
    { fullName: 'khalid_shields', age: 51, salary: 29181 },
    { fullName: 'charlotte_bechtelar', age: 15, salary: 40683 },
    { fullName: 'mozelle_corwin', age: 41, salary: 39444 },
    { fullName: 'blaze_renner', age: 28, salary: 32130 },
    { fullName: 'lilian_rogahn', age: 58, salary: 13129 },
    { fullName: 'cara_emard', age: 41, salary: 46718 },
    { fullName: 'kyler_maggio', age: 19, salary: 6268 },
    { fullName: 'bernita_christiansen', age: 45, salary: 27047 },
    { fullName: 'elody_grant', age: 34, salary: 6948 },
    { fullName: 'skylar_steuber', age: 19, salary: 5568 },
    { fullName: 'dannie_ruecker', age: 46, salary: 7217 },
    { fullName: 'ramiro_dooley', age: 45, salary: 38104 },
    { fullName: 'destiny_bruen', age: 42, salary: 47054 },
    { fullName: 'albina_hansen', age: 27, salary: 47550 },
    { fullName: 'albina_smith', age: 17, salary: 24912 },
    { fullName: 'kellie_kunde', age: 38, salary: 32896 },
    { fullName: 'lisandro_denesik', age: 62, salary: 18840 },
    { fullName: 'nels_goyette', age: 55, salary: 6875 },
    { fullName: 'luciano_blick', age: 19, salary: 14904 },
    { fullName: 'leora_west', age: 57, salary: 49004 },
    { fullName: 'baylee_flatley', age: 24, salary: 5373 },
    { fullName: 'tamara_ortiz', age: 41, salary: 25922 },
    { fullName: 'ursula_mills', age: 35, salary: 14234 },
    { fullName: 'alycia_nader', age: 34, salary: 23347 },
    { fullName: 'stefan_powlowski', age: 47, salary: 46853 },
    { fullName: 'holly_dickinson', age: 39, salary: 38663 },
    { fullName: 'antonetta_turcotte', age: 37, salary: 43430 },
    { fullName: 'pierce_cruickshank', age: 32, salary: 28591 },
    { fullName: 'marlee_reichel', age: 40, salary: 8889 },
    { fullName: 'allene_schimmel', age: 64, salary: 17746 },
    { fullName: 'carleton_franey', age: 17, salary: 23369 },
    { fullName: 'enoch_goyette', age: 19, salary: 29910 },
    { fullName: 'summer_deckow', age: 17, salary: 2939 },
    { fullName: 'damian_kulas', age: 25, salary: 34857 },
    { fullName: 'lew_kerluke', age: 18, salary: 39196 },
    { fullName: 'kathleen_klocko', age: 47, salary: 17795 },
    { fullName: 'jacky_armstrong', age: 17, salary: 24689 },
    { fullName: 'aidan_fadel', age: 28, salary: 6565 }
    ]
    
const capitalize = (arr)=>{
    return arr.map(first=>{
          return  first.charAt(0).toUpperCase() + first.slice(1);
            
        })
    }


const user = (userdata) =>{
    let myPromise = new Promise(function(myResolve, myReject){
        let total = 0
     let data = userdata.filter(function(a){
        return a.age >= 18;
       })


      let capital = data.map(function(letter){
          letter.fullName = capitalize(letter.fullName.split('_')).join(' ');
            return letter
        })
        data.map(function(t){
            total += t.salary
        })
        capital.push({Total:total})
     if (total > 0){
        console.log(capital)
        myResolve("success");
        
     }

     else{
        myReject("failed");
     }
      
    })

    myPromise.then(
        function(value){},
        function(error){}
 
    )
    return myPromise
    }
    console.log(user(userdata))

    //Sort the countries

const sortTheCountries = (countries,numberOfCountries) =>{
    countries.sort (function(a,b){
        return a.population-b.population

    })
    return countries.reverse().splice(0,numberOfCountries)
  }

 // console.log (sortTheCountries(countries,2))
  