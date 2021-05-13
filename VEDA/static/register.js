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
    isSubmited: false
  },
  methods: {
    onSubmit(event) {
      this.isSubmited = true

      if (this.validate_username & this.validate_name 
        & this.validate_password & this.validate_repeat_password & this.validate_dob) {
          return true
      } else {
        event.preventDefault()
      }
    },
    toLogin(event) {
      window.location.href = '/login'
    },
  },
  computed: {
    validate_email() {
      if (!this.isSubmited) return null
      
      const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(String(this.form.email).toLowerCase());
    },
    validate_username() {
      if (!this.isSubmited) return null

      return this.form.username.length > 4 
    },
    validate_name() {
      if (!this.isSubmited) return null

      return this.form.firstname.length > 0 && this.form.secondname.length > 0
    },
    validate_password() {
      if (!this.isSubmited) return null

      return this.form.password.length > 8
    },
    validate_repeat_password() {
      if (!this.isSubmited) return null

      return this.form.password === this.form.password_repeat
    },
    validate_gender() {
      if (!this.isSubmited) return null
      alert(this.form.gender)
      console.log(!!(this.form.gender === "F" | this.form.gender === "M" | this.form.gender === "O"));
      return !!(this.form.gender === "F" | this.form.gender === "M" | this.form.gender === "O")
    },
    validate_dob() {
      if (!this.isSubmited) return null

      return this.form.day_of_birthday !== ''
    }
  },
})