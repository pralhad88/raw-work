import simplejson as json

string="""
{
  "values" : [
    {
      "from" : "NameError",
      "to" : "NaamNahiHaiError"
    },
    {
      "from" : "unexpected indent",
      "to" : "Aapke code ki formatting theek nahi hai. Aapko apne code ki indentation (yaani spacing) theek karo, jisse ki python aapke code ko samajh jayein."
    }
  ]
}
"""

data=json.loads(string)
print(data)