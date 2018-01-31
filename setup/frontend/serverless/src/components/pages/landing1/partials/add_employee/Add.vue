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
import EmployeeModel from '../../../../../models/Employee.js'
import axios from 'axios'

export default {
    components: {
        modalvue
    },

    data: function() {
        return {
            employee: new EmployeeModel(null, 'John', 'Smith')
        }
    },

    methods: {
        saveFunction(emp) {
            console.log(emp)
            axios.post('https://iaeoli1xlg.execute-api.us-west-1.amazonaws.com/prod/employee/add', {
                'first': emp.first,
                'last': emp.last,
                'email': emp.email
            })
            .then(response => {
                console.log(response)
            })
        }
    }
}
</script>
