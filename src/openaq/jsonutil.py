
class JSONUtil:

    def __init__(self):
        """
        This class is to process the output JSON of OpenAQ API and convert it into Dataframe
        """

    def format_latest_json(self, results):
        allVals = []
        if results == {}:
            return
        for each_loc in results:
            allKeys = each_loc.keys()

            if 'measurements' in each_loc.keys():
                loc_data = {}
                """if 'distance' not in allKeys:
                  loc_data['distance'] = np.NaN
                if 'coordinates' not in allKeys:
                  loc_data['latitude'] = np.NaN
                  loc_data['longitude'] = np.NaN
                """
                for keyVal in allKeys:
                    if keyVal not in ['measurements','coordinates']:
                        loc_data[keyVal] = each_loc[keyVal]
                    if keyVal == 'coordinates':
                        coordVal = each_loc[keyVal]
                        loc_data['latitude'] = coordVal['latitude']
                        loc_data['longitude'] = coordVal['longitude']
                for each_measure in each_loc['measurements']:
                    df_row = {}
                    df_row.update(loc_data)
                    df_row.update(each_measure)
                    allVals.append(df_row)
        return allVals