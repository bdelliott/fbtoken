function initStubFacebookAPI() {

    // operations:
    FB = {
        login: loginStub,
    };

    console.log(document);
    postInit();
}

function loginStub(callback) {
    console.log("loginStub");

    credentials = {
        accessToken: "1234567890",
        expiresIn: "5500",
        userID: "54321"
    }

    response = { authResponse: credentials };
    callback(response);
}
