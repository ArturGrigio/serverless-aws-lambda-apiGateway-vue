import Vue from 'vue'
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        employeeList: []
    },

    mutations: {
        setEmployees(state, payload) {
            state.employeeList = payload
        },
        updateEmployee(state, employee) {
            state.employeeList.some(emp => {
                if (emp.id === employee.id) {
                    emp.first = employee.first
                    emp.last = employee.last
                    emp.email = employee.email
                    return true;
                }
                return false;
            })
        },
        deleteEmployee(state, id) {
            state.employeeList.some((emp, index) => {
                if (emp.id === id) {
                    state.employeeList.splice(index, 1)
                    return true;
                }
                return false;
            })
        },
        pushEmployee(state, employee) {
            state.employeeList.push(employee)
        }
    },

    actions: {
        setEmployees({commit}, payload) {
            commit('setEmployees', payload)
        },
        updateEmployee({commit}, payload) {
            commit('updateEmployee', payload)
        },
        deleteEmployee({commit}, payload) {
            commit('deleteEmployee', payload)
        },
        pushEmployee({commit}, payload) {
            commit('pushEmployee', payload)
        }
    },
    strict: true
})
