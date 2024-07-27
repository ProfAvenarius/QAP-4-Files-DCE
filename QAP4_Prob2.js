// Description: QAP 4 Problem 3 - Create a JS object for a motel customer and output
//              a paragraph that is populated with attributes from the object
// Author: David C Elliott
// Date: July 18 - 26th, 2024

// JS object defined below

const Motel_Guest = {
    first_name: 'Bob',
    last_name: 'Loblaw',
    b_date: '1980',
    gender: 'male',
    address: {
        street: '13 West St.',
        city: 'St. John\'s',
        province: 'NL',
        post_code: 'A1A1A1',
        country: `CANADA`,
        },
    phone_num_h: '709-123-1234',
    phone_num_c: '709-321-4321',
    e_mail: 'BobLoblaw@mail.com',
    pay_meth: ['Credit Card','Mastercard','0010 1050 5150 2551', '07/26'],
    room_pref: ['307', '305' ,'303'],
    reservation: {
        check_in: '2024-07-17',
        check_out: '2024-07-23',
    },

    fullName: function() {
        return `${this.first_name} ${this.last_name}`
    },

    getAge: function(){
        const today = new Date();
        return today.getFullYear() - this.b_date;
    },    

    getStay: function() {
        const f_day = new Date(this.reservation.check_in);
        const first_day = f_day.getDate()
        const l_day = new Date (this.reservation.check_out);
        const last_day = l_day.getDate()
        return last_day - first_day
       
    }

}

// l_array = Object.entries(Motel_Guest).length

len_array = Object.entries(Motel_Guest).length
guest_array = Object.entries(Motel_Guest)
address_array  = Object.entries(Motel_Guest)[4]

guest_key = Object.keys(Motel_Guest)
guest_val = Object.values(Motel_Guest)
// Display the object in the console, as 

// an object
console.log(Motel_Guest);
// an array
console.log(guest_array);
// an array within the array, the address
console.log(address_array);

//deconstructing attributes used in the script below
const {last_name, gender, reservation, room_pref, pay_meth, address, phone_num_c, phone_num_h} = Motel_Guest


//Refering to the object to determine output with a if/else statement
if (gender == "male") {
    prefix = "Mr."
} else if (gender == "female") {
    prefix = "Ms."
} else {
    prefix = ""
}


//a descriptive paragraph with embedded characteristics
quote = `The ${gender} guest's name was ${last_name}, ${Motel_Guest.fullName()}.  Janet was working behind the front desk, she
glanced down at his reservation, a ${Motel_Guest.getStay()} day stay beginning on the ${reservation.check_in}. 
"Unfortunately ${prefix} ${last_name} , your regular room ${room_pref[0]} is not available tonight, but we do have ${room_pref[1]} ready for you 
and you have your choice of either for the rest of your ${Motel_Guest.getStay()} day stay..."
He seemed younger than his ${Motel_Guest.getAge()} years, and smiled at the news, "That would be fine" he said as he laid down his ${pay_meth[0]}.
"You take ${pay_meth[1]}?" he asked, his ${address.city} accent in full display.  "Of course" Janet replied, " Let's just confirm these details..." 
After confiming the credit card digits ${pay_meth[2]} and expiry date ${pay_meth[3]}, she asked him "Is ${phone_num_c} the correct cell? And ${phone_num_h} the home phone?..."  In no time now he would be warm in his room...`

document.getElementById("output").innerHTML = quote;



// Lets use a for loop to display the entire object in html
let outputHTML = '';

for (let key in Motel_Guest) {
    if (typeof Motel_Guest[key] === 'function') {
        outputHTML += `<p>${key}: ${Motel_Guest[key]()}</p>`;
    } else if (typeof Motel_Guest[key] === 'object') {
        if (Array.isArray(Motel_Guest[key])) {
            outputHTML += `<p>${key}: ${Motel_Guest[key].join(', ')}</p>`;
        } else {
            let address = '';
            for (let subKey in Motel_Guest[key]) {
                address += `${Motel_Guest[key][subKey]}, `;
            }
            outputHTML += `<p>${key}: ${address.slice(0, -2)}</p>`;
        }
    } else {
        outputHTML += `<p>${key}: ${Motel_Guest[key]}</p>`;
    }
}

// Set the output HTML to the guestInfo div
document.getElementById('guestInfo').innerHTML = outputHTML;