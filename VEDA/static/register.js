var application = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        username: '',
        firstname: '',
        secondname: '',
        email: '',
        password: '',
        password_repeat: '',
        day_of_birthday: ''
    },
    methods: {
        onSubmit(event) {
            // event.preventDefault()
        },
        toLogin(event) {
            window.location.href = '/login'
        }
    },
    computed: {
        validate_username() {
            return this.username.length > 4 
        },
        validate_name() {
            return this.firstname.length > 0 && this.secondname.length > 0
        },
        validate_password() {
            return this.password.length > 8
        },
        validate_repeat_password() {
            return this.password === this.password_repeat
        },
        validate_dob() {
            return this.day_of_birthday !== ''
        }
    }
})