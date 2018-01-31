<template>
    <span>
        <modalvue
            :function="saveFunction"
            :modalemployee="employee"
            modaltype="Add">
            <a class="waves-effect waves-light btn modal-trigger green" href="#modal">
                <i class="left mdi mdi-plus-circle"></i>
                ADD EMPLOYEE
            </a>
        </modalvue>
    </span>
</template>

<script>
import modalvue from '../modal/Modal.vue'
import Employee from '../../../../../models/Employee.js'
import axios from 'axios'

export default {
    components: {
        modalvue
    },

    data: function() {
        return {
            employee: new Employee()
        }
    },

    methods: {
        saveFunction(emp) {
            console.log(emp)
            let self = this
            axios.post('https://iaeoli1xlg.execute-api.us-west-1.amazonaws.com/prod/employee/add', {
                'first': emp.first,
                'last': emp.last,
                'email': emp.email
            })
            .then(response => {
                emp.id = response.data
                self.$store.dispatch('pushEmployee', emp)
            })
        }
    }
}
</script>
