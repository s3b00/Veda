var login = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        username: '', 
        password: '',
        usernameValid: null,
        passwordValid: null,
    },
    methods: {
        validateData() {
            this.usernameValid = this.username.length > 0

            this.passwordValid = this.password.length > 0

            return this.usernameValid & this.passwordValid
        },
        onSubmit(event) {
            if (this.validateData()) {
                return true
            } else {
                event.preventDefault()
            }
        },
        toRegister(event) {
            window.location.href = '/registration'
        }
    },
})