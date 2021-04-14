var login = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        email: '',
        password: '',
    },
    methods: {
        onSubmit(event) {
            event.preventDefault()
            alert(JSON.stringify(this.data))
        },
        toRegister(event) {
            window.location.href = '/registration'
        }
    },
})