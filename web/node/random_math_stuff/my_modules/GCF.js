// GCF.js

const GCF = (a, b) => {
	if (a % b == 0){
		return b;
	}
	return GCF(b, a%b);

};
module.exports = {GCF}
console.log (GCF)

