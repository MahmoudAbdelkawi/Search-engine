import SortData.SortData;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.util.*;

public class ReducerIndex extends  Reducer<Text, Text, Text, Text>{
    private final Text allFilesConcatValue = new Text();

    public static Double getRankFromString(String url){

        int startIndex = url.indexOf("~Rank=")+6;
        int endIndex = url.indexOf(";");
        String Rank = new String();
        for (int i = startIndex; i < endIndex ; i++) {

            Rank += url.charAt(i);
        }
        if(Rank.equals(""))
            return 0.0;
        else
            return Double.parseDouble(Rank);
    }

    public static String sortData(String data){
        Map<Double , String> orderedData = new HashMap<Double,String>();
        String[] links = data.split(";");
        for(String link : links){
            if (link.length()>1)
                orderedData.put(getRankFromString(link+";") , link+";");
        }
        TreeMap<Double,String>sortedLinks =new TreeMap<>();
        sortedLinks.putAll(orderedData);
        String value = new String();
        for (Map.Entry<Double,String> entry :sortedLinks.entrySet() ) {
            value+= entry.getValue();
        }
        return value;
    }


    @Override
    protected void reduce(Text key, Iterable<Text> values,
                          Context context) throws java.io.IOException ,InterruptedException {

        StringBuilder filelist = new StringBuilder("");


        // Sort Links with their ranks
        for(Text value:values) {
                filelist.append(value.toString().replaceAll("null" ,"0.0")+";");
        }


        allFilesConcatValue.set(sortData(filelist.toString()));
        context.write(key, allFilesConcatValue);
    };

}
