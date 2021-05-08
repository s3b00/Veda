let group = new Vue({
    delimiters: ['[[', ']]'],
    el: '#group',
    data: {
        items: [
            'БДиСУБД',
            'ОП',
            'КПиЯП',
            'ППО',
            'Физкультура'
        ],
        noticeManager: {
            notice: '',
            noticeValid: null
        },
    },
    methods: {
        addNotice(event) {
            this.noticeManager.noticeValid = this.noticeManager.notice.length > 0
            
            if (this.noticeManager.noticeValid) {
                return true
            } else {
                event.preventDefault()
            }
        }
    }
})