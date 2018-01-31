<template>
    <span>
        <div class="spacer-4"></div>
        <div class="spacer-4"></div>

        <div class="container row no-padding">

            <h2 id="add-employees" class="thin">My Employees</h2>

            <div class="col s12">
                <addemployeevue></addemployeevue>
            </div>
            <div class="col s12 collection">
                <div v-for="emp in employeeList" v-bind:key="emp.employeeId" class="collection-item">
                    <employeevue
                        :employee="emp">
                    </employeevue>
                </div>
            </div>

        </div>

        <div class="spacer-4"></div>
        <div class="spacer-4"></div>
    </span>
</template>

<script>
import addemployeevue from './partials/add_employee/Add.vue'
import employeevue from './partials/employee/Employee.vue'
import axios from 'axios'

export default {
    components: { addemployeevue, employeevue },
    data() {
        return {
            employeeList: []
        }
    },

    methods: {
        getEmployees() {
            let self = this
            axios.get('https://iaeoli1xlg.execute-api.us-west-1.amazonaws.com/prod/employee/all')
            .then(response => {
                console.log(response.data)
                response.data.forEach(emp => {
                    self.employeeList.push(emp)
                })
            })
            .catch(error => {
                console.log(error)
            })
        }
    },

    mounted() {
        this.getEmployees()
    }
}
</script>
