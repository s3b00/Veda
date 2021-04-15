var registration = new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  data: {
    form: {
    username: '',
    firstname: '',
    secondname: '',
    hobbies: '',
    email: '',
    address: '',
    password: '',
    password_repeat: '',
    day_of_birthday: ''
    }       
  },
  methods: {
    onSubmit(event) {
      console.log(this.validate_username())
      // if (validate_username() && validate_name() && validate_password() && validate_repeat_password() && validate_dob()) {
      //     return true
      // }

      // // event.preventDefault()
      // alert(JSON.stringify(this.form))

      event.preventDefault()
    },
    toLogin(event) {
      window.location.href = '/login'
    }
  },
  computed: {
    validate_username() {
      return this.form.username.length > 4 
    },
    validate_name() {
      return this.form.firstname.length > 0 && this.form.secondname.length > 0
    },
    validate_password() {
      return this.form.password.length > 8
    },
    validate_repeat_password() {
      return this.form.password === this.form.password_repeat
    },
    validate_dob() {
      return this.form.day_of_birthday !== ''
    }
  },
})