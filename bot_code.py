    def do_admin_command(self, endpoint, payload):
        """
        A command to perform admin api
        """
        #setting up headers here:
        headers = {
            "Accept": "application/json",
            "circle-token": circle_token,
            "Content-Type": 'application/x-www-form-urlencoded'
        }

        try:

            res = requests.post(url = endpoint, params = payload)
            #To throw (or raise) an exception, use the raise keyword.
            res.raise_for_status()
#Logs a message with integer level level on this logger. 
            self.log.info(res)
            res = res.json()
            self.log.info(res)
            return "Circle says: We successfully whitelisted your branch: {}".format("master")
#you can choose to throw an exception if a condition occurs
# err for this except statement must be unique which is why errc is the reference name for the ConnectionError.
        except requests.exceptions.HTTPError as err:
            self.log.info(err)
            return "Circle says: `#{0}`:\n`{1}`".format(err.response.status_code, err)
        except requests.ConnectionError as errc:
            self.log.info(errc)
            return "Circle says: `#{errc}`"

            #   extracting data in json format

