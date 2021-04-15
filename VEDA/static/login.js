var login = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        username: '', 
        password: '',
    },
    methods: {
        onSubmit(event) {
        },
        toRegister(event) {
            window.location.href = '/registration'
        }
    },
})