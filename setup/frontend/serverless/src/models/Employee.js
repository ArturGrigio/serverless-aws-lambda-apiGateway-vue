export default class Employee {
    constructor(employeeId, first, last, email) {
        this.employeeId = employeeId || '';
        this.first = first || '';
        this.last = last || '';
        this.email = email || '';
    }
}
