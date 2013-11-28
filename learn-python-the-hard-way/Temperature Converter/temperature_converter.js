/**
 * Created with PyCharm.
 * User: Dal
 * Date: 11/27/13
 * Time: 8:03 PM
 * To change this template use File | Settings | File Templates.
 */

var convertfrom = prompt('Do you want to convert from Fahrenheit or Celsius?').toLowerCase();

if (convertfrom === 'fahrenheit') {
    var far = prompt('What is the current temperature in Fahrenheit?');
    console.log('Your temperature in Celsius is ' + Math.round((parseFloat(far)- 32) * (5/9)));
} else if (convertfrom === 'celsius') {
    var cel = prompt('What is the current temperature in Celsius?');
    console.log('Your temperature in Fahrenheit is ' + Math.round(parseFloat(cel) * (9/5) + 32));
} else {
    console.log('Input Fahrenheit or Celsius dammit!');
}
