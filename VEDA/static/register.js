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
      gender: null,
      password: '',
      password_repeat: '',
      day_of_birthday: ''
    },
    genderValid: null
  },
  methods: {
    onSubmit(event) {
      if (this.validate_username & this.validate_name 
        & this.validate_password & this.validate_dob) {
          return true
      } else {
        event.preventDefault()
      }
    },
    toLogin(event) {
      window.location.href = '/login'
    },
    validateGender() {
      this.genderValid = this.form.gender === "F" | this.form.gender === "M" | this.form.gender === "O"
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