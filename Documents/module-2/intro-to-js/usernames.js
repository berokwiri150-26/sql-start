require("datejs");

function combineUsers(...groups) {
    let combinedObject = { users:[] };
    for (const group of groups) {
        combinedObject.users = [...combinedObject.users, ...group];
    }
    combinedObject.merge_date = new Date().toString("07/04/2026");
    return combinedObject;
}
const group1 = ["Clyde", "Chantal", "Timothy"];
const group2 = ["Titus", "Joseph", "Alvin"];
const group3 = ["Bernd", "Andrew", "Wambua"];

const combinedUsers = combineUsers(group1, group2, group3);
console.log(combinedUsers);

module.exports = combineUsers;
