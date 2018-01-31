<template>
    <span>
        <div class="spacer-4"></div>
        <div class="spacer-4"></div>

        <div class="container row no-padding">

            <h1 class="thin">My Employees</h1>

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
import EmployeeModel from '../../../models/Employee.js';

export default {
    components: { addemployeevue, employeevue },
    data() {
        return {
            employeeList: []
        }
    },

    methods: {
        getEmployees() {
            this.employeeList.push(new EmployeeModel(1, 'John', 'Smith', 'asfasf@asdfadsf.com'))
            this.employeeList.push(new EmployeeModel(2, 'John', 'Smith', 'asfasf@asdfadsf.com'))
            this.employeeList.push(new EmployeeModel(3, 'John', 'Smith', 'asfasf@asdfadsf.com'))
            this.employeeList.push(new EmployeeModel(4, 'John', 'Smith', 'asfasf@asdfadsf.com'))
            this.employeeList.push(new EmployeeModel(5, 'John', 'Smith', 'asfasf@asdfadsf.com'))
        }
    },

    mounted() {
        this.getEmployees()
    }
}
</script>
