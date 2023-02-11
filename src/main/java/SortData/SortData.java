package SortData;

import java.util.*;

public class SortData {
    public static List<String>word = new ArrayList<>();

//    public static List<String>
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
    public static List<String> getRanks(Map ranks) {
        List<Map.Entry<String, Double>> list = new ArrayList<>(ranks.entrySet());
        list.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));
        List<String> orderedValue = new ArrayList<>();
        for (Map.Entry<String, Double> entry : list) {
            orderedValue.add(entry.getKey());
        }
        return orderedValue;
    }
    public static List<String> getLinkOrdered(List<String> links){
        Map<String, Double> ranks = new HashMap<>();
        for (String link : links){
            ranks.put(link,getRankFromString(link));
        }
//        int i=0;
        for (String value : getRanks(ranks))
        {

            word.add(value);
//            i++;
        }
        return word;
    }

    public static void main(String[] args){





        List <String> text = new ArrayList<>();
        text.add("https://www.10best.com/destinations/illinois/chicago/~Number=1~Rank=0.06767170956963069;");
        text.add("https://www.usatoday.com/storytelling/coronavirus-reopening-america-map/~Number=2~Rank=0.07031291107544306;");
        text.add("https://nypost.com/article/where-is-sports-betting-legal-in-united-states/~Number=1~Rank=0.1345175777666681;");
        for (String txt : getLinkOrdered(text))
            System.out.println(txt);

    }
}