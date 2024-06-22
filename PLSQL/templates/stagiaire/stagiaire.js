const form = document.getElementById('form');
const fullname = document.getElementById('fullName');
const age = document.getElementById('age');
const email = document.getElementById('email');
const gender = document.getElementById('gender');
const password = document.getElementById('password');
const password2 = document.getElementById('checkPassword');
const phoneNumber = document.getElementById("phoneNumber");
const submit = document.getElementById("submit");


// !add event listener
form.addEventListener("submit", (e) => {
    e.preventDefault();
  
    // check input & observed validation
    checkInput();
  });
  function checkInput() {
    // get all value in required field
    // use trim() function for remove whitespace
    const fullNameValue = fullName.value.trim();
    // const usernameValue = userName.value.trim().toLowerCase();
    const emailValue = email.value.trim();
    const genderValue = gender.value;
    const ageValue = age.value.trim();
    const phoneNumberValue = phoneNumber.value.trim();
    const passwordValue = password.value.trim();
    const checkPasswordValue = checkPassword.value.trim();
    if (fullNameValue === "") {
        // show error message
        // add error class
        setErrorMessage(fullName, "Full Name field can't be blank. Required this field.");
    
        // focus element
        fullName.focus();
      } else if (fullNameValue.length < 3 || fullNameValue.length > 50) {
        setErrorMessage(fullName, "This field minimum character is 3. Please input at this range.");
    
        // focus element
        fullName.focus();
      } else {
        // add success class
        setSuccessMessage(fullName);
      }

      // !email validation check
       if (emailValue === "") {
        // show error message
        // add error class
        setErrorMessage(email, "Email field can't be blank. Required this field.");
    
        // focus element
        email.focus();
      } else if (!isValidateEmail(emailValue)) {
        setErrorMessage(email, "Sorry! Your define email is not valid.");
    
        // focus element
        email.focus();
      } else {
        // add success class
        setSuccessMessage(email);
      }
      

      // !phone validation check
      if (phoneNumberValue === "") {
        // show error message
        // add error class
        setErrorMessage(phoneNumber, "Phone Number field can't be blank. Required this field.");
    
        // focus element
        phoneNumber.focus();
      } else if (phoneNumberValue.length < 10) {
        setErrorMessage(phoneNumber, "This field minimum maximum character is 10.");
    
        // focus element
        phoneNumber.focus();
      } else {
        // add success class
        setSuccessMessage(phoneNumber);
      }
     //age validation check
      if (ageValue === "") {
        // show error message
        // add error class
        setErrorMessage(age, "Age field can't be blank. Required this field.");
    
        // focus element
        password.focus();
      } else if (ageValue < 18 || ageValue.length > 2) {
        setErrorMessage(age, "This field minimum age is 18 . Please input at this range.");
    
        // focus element
        password.focus();
      } else {
        // add success class
        setSuccessMessage(age);
      }  
    

 // !password validation check
if (passwordValue === "") {
    // show error message
    // add error class
    setErrorMessage(password, "Password field can't be blank. Required this field.");

    // focus element
    password.focus();
  } else if (passwordValue.length < 8 || passwordValue.length > 20) {
    setErrorMessage(password, "This field minimum character is 8.");

    // focus element
    password.focus();
  } else {
    // add success class
    setSuccessMessage(password);
  }  

  // !retype password validation check
  if (checkPasswordValue === "") {
    // show error message
    // add error class
    setErrorMessage(checkPassword, "Password field can't be blank. Required this field.");

    // focus element
    checkPassword.focus();
  } else if (checkPasswordValue.length < 6 || checkPasswordValue.length > 20) {
    setErrorMessage(checkPassword, "This field minimum character is 8.");

    // focus element
    checkPassword.focus();
  } else if (passwordValue !== checkPasswordValue) {
    setErrorMessage(checkPassword, "Sorry! Your define password and Retype password not match. Please input correct password.");

    // focus element
    checkPassword.focus();
  } else {
    // add success class
    setSuccessMessage(checkPassword);
  }

  if(genderValue=='default'){

    setErrorMessage(gender, "Select your gender");
    
    }else {
        // add success class
        setSuccessMessage(gender);
      }

  }
  // !input error message show function
function setErrorMessage(input, message) {
    // select input field parentELement
    const formControl = input.parentElement; // parentELement = .form-control
    const small = formControl.querySelector("small");
  
    // add error message inside small
    small.innerText = message;
  
    // add error class
    formControl.className = "form-control error";
  }
  
  // !input success message show function
  function setSuccessMessage(input) {
    // select input field parentELement
    const formControl = input.parentElement; // parentELement = .form-control
  
    // add success class
    formControl.className = "form-control success";
  }
  
  // !proper username validation check
  function isUserNameValid(username) {
    /* 
      Usernames can only have: 
      - Lowercase Letters (a-z) 
      - Numbers (0-9)
      - Dots (.)
      - Underscores (_)
    */
    const res = /^[a-z0-9_\.]+$/.exec(username);
    const valid = !!res;
    return valid;
  }
  
  // !proper email validation check
  function isValidateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
  }





    